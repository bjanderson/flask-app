import json

from app.apis.crud_api import CrudAPI
from flask import request


class PostApi(CrudAPI):
    def __init__(self, app, db):
        super().__init__(app, db)

    @property
    def route(self):
        return "/post"
