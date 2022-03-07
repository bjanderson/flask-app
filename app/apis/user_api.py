import json

# from app.apis.crud_api import CrudAPI
from flask import request

# REST API METHODS:  https://restfulapi.net/http-methods/
# HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status


# class UserApi(CrudAPI):
class UserApi():
    def __init__(self, app, db):
        # super().__init__(app, db)
        self.app = app
        self.db = db
        self.configure_routes(app)

    # @property
    # def route(self):
    #     return "/user"

    def get(self, pk=None):
        if pk is not None:
            # get one item from the database
            item = self.db.get(pk)
            if item is not None:
                item = item.__dict__
            response = self.app.response_class(
                response=json.dumps(item), status=200, mimetype="application/json"
            )
            return response

        else:
            # get all items from the database
            items = self.db.get_all()
            items = list(map(lambda item: item.__dict__, items))
            response = self.app.response_class(
                response=json.dumps(items), status=200, mimetype="application/json"
            )
            return response

    def post(self):
        #create a new item in the database
        data_string = request.get_data()
        data = json.loads(data_string)

        item = self.db.insert(data)
        if item is None:
            response_item = json.dumps(
                {"message": f"Could not insert data {json.loads(data_string)}"}
            )
            response = self.app.response_class(
                response=response_item, status=500, mimetype="application/json"
            )
            return response
        else:
            response_item = json.dumps(item.__dict__)
            response = self.app.response_class(
                response=response_item, status=200, mimetype="application/json"
            )
            return response

    def put(self, pk=None):
        # update an item in the database
        data_string = request.get_data()
        data = json.loads(data_string)

        item = self.db.update(data)
        if item is None:
            response_item = json.dumps(
                {"message": f"Could not update data {json.loads(data_string)}"}
            )
            response = self.app.response_class(
                response=response_item, status=500, mimetype="application/json"
            )
            return response
        else:
            response_item = json.dumps(item.__dict__)
            response = self.app.response_class(
                response=response_item, status=200, mimetype="application/json"
            )
            return response

    def delete(self, pk=None):
        # remove an item from the database

        self.db.delete(pk)
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
