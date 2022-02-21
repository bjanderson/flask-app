from app.models.user import User

from .crud_db import CrudDB


class UserDB(CrudDB):
    @property
    def table_name(self):
        return "user"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the User class or the mappings will break
        return [
            "email TEXT NOT NULL",
            "name TEXT NOT NULL",
            "pk TEXT NOT NULL PRIMARY KEY",
        ]

    def create_item(self, tup):
        user = User.from_tuple(tup)
        return user
