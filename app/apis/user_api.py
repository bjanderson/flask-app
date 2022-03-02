import json

from flask import request

# REST API METHODS:  https://restfulapi.net/http-methods/
# HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


class UserApi():
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.configure_routes(app)

    def get(self, pk=None):
        if pk is not None:
            # get one item from the database
            print("\nGet One")
            print(f"pk: {pk}")

            # item = {"name": "user 1"}
            # response = self.app.response_class(
            #     response=json.dumps(item), status=200, mimetype="application/json"
            # )
            # return response

            item = self.db.get(pk)
            if item is not None:
                item = item.__dict__
            response = self.app.response_class(
                response=json.dumps(item), status=200, mimetype="application/json"
            )
            return response

        else:
            # get all items from the database
            print("\nGet All")

            # items = [{"name": "user 1"}, {"name": "user 2"}, {"name": "user 3"}]
            # response = self.app.response_class(
            #     response=json.dumps(items), status=200, mimetype="application/json"
            # )
            # return response

            items = self.db.get_all()
            items = list(map(lambda item: item.__dict__, items))
            response = self.app.response_class(
                response=json.dumps(items), status=200, mimetype="application/json"
            )
            return response

    def post(self):
        data_string = request.get_data()
        print("Post")
        print(data_string)
        data = json.loads(data_string)
        response = self.app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response


    def put(self, pk=None):
        data_string = request.get_data()
        print("\nPut")
        print(f"pk: {pk}")
        print(data_string)
        data = json.loads(data_string)
        response = self.app.response_class(
            response=json.dumps(data), status=200, mimetype="application/json"
        )
        return response

    def delete(self, pk=None):
        print("\nDelete")
        print(f"pk: {pk}")
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
