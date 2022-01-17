import json

from flask import request


class UserApi():
    def __init__(self, app):
        self.app = app
        self.configure_routes(app)

    def get(self, pk=None):
        if pk is not None:
            print(f"GET: one by pk: {pk}")
            item = {"name": "user 1"}
            response = self.app.response_class(
                response=json.dumps(item), status=200, mimetype="application/json"
            )
            return response
        else :
            print("GET: all")
            items = [{"name": "user 1"}, {"name": "user 2"}]
            response = self.app.response_class(
                response=json.dumps(items), status=200, mimetype="application/json"
            )
            return response

    def post(self):
        data_string = request.get_data()
        data = json.loads(data_string)
        print(f"POST: data: {data}")
        response = self.app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response

    def put(self, pk=None):
        data_string = request.get_data()
        data = json.loads(data_string)
        print(f"PUT: pk, data: {pk}, {data}")
        response = self.app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response

    def delete(self, pk=None):
        print(f"DELETE: pk: {pk}")
        data = {"deleted": True, "pk": pk}
        response = self.app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response

    def configure_routes(self, app):
        app.add_url_rule("/user", "user-get", self.get, methods=["GET"])
        app.add_url_rule(
            "/user/<pk>", "user-get-pk", self.get, methods=["GET"]
        )
        app.add_url_rule(
            "/user", "user-post", self.post, None, methods=["POST"]
        )
        app.add_url_rule(
            "/user/<pk>", "user-put", self.put, None, methods=["PUT"]
        )
        app.add_url_rule(
            "/user/<pk>",
            "user-delete",
            self.delete,
            None,
            methods=["DELETE"],
        )
