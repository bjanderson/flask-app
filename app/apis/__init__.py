from app.db.user_db import UserDB

from .user_api import UserApi


def init_apis(app, db):

    user_db = UserDB(db)
    UserApi(app, user_db)
