import json

from flask import request

# REST API METHODS:  https://restfulapi.net/http-methods/
# HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


class UserApi():
    def __init__(self, app):
        self.app = app
        self.configure_routes(app)

    def get(self):
            item = {"name": "user 1"}
            response = self.app.response_class(
                response=json.dumps(item), status=200, mimetype="application/json"
            )
            return response

    def configure_routes(self, app):
        app.add_url_rule("/user", "user-get", self.get, methods=["GET"])
