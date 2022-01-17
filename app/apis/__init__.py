from .user_api import UserApi


def init_apis(app):
    UserApi(app)
