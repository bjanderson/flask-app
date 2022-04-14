from app.models.post import Post

from .crud_db import CrudDB


class PostDB(CrudDB):
    @property
    def table_name(self):
        return "post"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the post class or the mappings will break
        return [
            "content TEXT NOT NULL",
            "title TEXT NOT NULL",
            "insertedAt INT NOT NULL",
            "modifiedAt INT NOT NULL",
            "userPk TEXT NOT NULL",
            "pk TEXT NOT NULL PRIMARY KEY",
            "FOREIGN KEY(userPk) REFERENCES user(pk)"
        ]

    def create_item(self, tup):
        post = Post.from_tuple(tup)
        return post
