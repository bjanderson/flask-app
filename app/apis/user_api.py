import json

from app.apis.crud_api import CrudAPI
from flask import request

# REST API METHODS:  https://restfulapi.net/http-methods/
# HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


class UserApi(CrudAPI):
    def __init__(self, app, db):
        super().__init__(app, db)

    @property
    def route(self):
        return "/user"
