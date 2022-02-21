import uuid
from abc import ABC, abstractmethod, abstractproperty


class CrudDB(ABC):
    def __init__(self, db):
        self.db = db
        self.create_table()

    @abstractproperty
    def table_name(self):
        pass

    @abstractproperty
    def table_column_definitions(self):
        pass

    @property
    def table_columns(self):
        cols = filter(
            lambda col: self.is_table_column(col),
            self.table_column_definitions,
        )
        cols = list(map(lambda col: col.split(" ")[0], cols))
        return cols

    def is_table_column(self, col):
        return not col.startswith("PRIMARY KEY") and not col.startswith("FOREIGN KEY")

    @abstractmethod
    def create_item(self, tup):
        pass

    def create_table(self):
        stmt = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({', '.join(self.table_column_definitions)});"
        self.db.execute(stmt)

    def table_exists(self):
        stmt = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.table_name}';"
        result = self.db.fetchone(stmt)
        result = result is not None and result[0] == self.table_name
        return result

    def get_column_names(self):
        return ", ".join(self.table_columns)

    def get_item_values(self, item):
        if isinstance(item, dict):
            d = item
        else:
            d = item.__dict__

        values = []
        for col in self.table_columns:
            try:
                values.append(d[col])
            except (KeyError):
                values.append(None)

        vals = ", ".join(f"'{v}'".replace("'None'", "null") for v in values)
        return vals

    def insert(self, item):
        try:
            item["pk"] = uuid.uuid4()
            cols = self.get_column_names()
            vals = self.get_item_values(item)
            stmt = f"INSERT INTO {self.table_name} ({cols}) VALUES ({vals})"
            self.db.execute(stmt)
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)
        return self.get(item["pk"])

    def update(self, item):
        setters = self.get_update_setters(item)
        stmt = f"UPDATE {self.table_name} SET {setters} WHERE pk = '{item['pk']}'"
        self.db.execute(stmt)
        return self.get(item["pk"])

    def get_update_setters(self, item):
        cols = self.table_columns
        vals = self.get_item_values(item).split(", ")
        setters = []
        for c, v in zip(cols, vals):
            setters.append(f"{c} = {v}")
        setters = filter(lambda setter: not setter.startswith("pk = "), setters)
        return ", ".join(setters)

    def get_all(self):
        cols = self.get_column_names()
        stmt = f"SELECT {cols} FROM {self.table_name}"
        result = self.db.fetchall(stmt)
        items = []
        if result is not None:
            for res in result:
                item = self.create_item(res)
                items.append(item)
        return items

    def get(self, pk):
        cols = self.get_column_names()
        stmt = f"SELECT {cols} FROM {self.table_name} WHERE pk = '{pk}'"
        result = self.db.fetchone(stmt)
        if result is not None:
            result = self.create_item(result)
        return result

    def delete(self, pk):
        stmt = f"DELETE FROM {self.table_name} WHERE pk = '{pk}'"
        self.db.execute(stmt)
