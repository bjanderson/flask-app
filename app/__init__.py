from flask import Flask

app = Flask(__name__)

from app import routes
from app.apis import init_apis

init_apis(app)
