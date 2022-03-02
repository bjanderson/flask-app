# https://flask.palletsprojects.com/en/1.1.x/views/
import json
from abc import ABC, abstractproperty

from flask import request


class CrudAPI(ABC):
    def __init__(self, app, db):
        self.app = app
        self.db = db
        self.configure_routes(app)

    @abstractproperty
    def route(self):
        pass

    @property
    def id(self):
        return str(self.route).replace("/", "")

    def get(self, pk=None):
        if pk is not None:
            item = self.db.get(pk)
            if item is not None:
                item = item.__dict__
            response = self.app.response_class(
                response=json.dumps(item), status=200, mimetype="application/json"
            )
            return response
        else:
            items = self.db.get_all()
            items = list(map(lambda item: item.__dict__, items))
            response = self.app.response_class(
                response=json.dumps(items), status=200, mimetype="application/json"
            )
            return response

    def post(self):
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
        self.db.delete(pk)
        return f"delete - pk: {pk}"

    def configure_routes(self, app):
        app.add_url_rule(f"{self.route}", f"{self.id}-get",
                         self.get, methods=["GET"])
        app.add_url_rule(
            f"{self.route}/<pk>", f"{self.id}-get-pk", self.get, methods=["GET"]
        )
        app.add_url_rule(
            f"{self.route}", f"{self.id}-post", self.post, None, methods=["POST"]
        )
        app.add_url_rule(
            f"{self.route}", f"{self.id}-put", self.put, None, methods=["PUT"]
        )
        app.add_url_rule(
            f"{self.route}/<pk>",
            f"{self.id}-delete",
            self.delete,
            None,
            methods=["DELETE"],
        )
