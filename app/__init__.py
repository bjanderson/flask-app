from flask import Flask

from .db import DB

app = Flask(__name__)

from app import routes
from app.apis import init_apis

db = DB("data/flask-app.db")
init_apis(app, db)
