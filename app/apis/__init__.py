from app.db.post_db import PostDB
from app.db.user_db import UserDB

from .post_api import PostApi
from .user_api import UserApi


def init_apis(app, db):

    user_db = UserDB(db)
    UserApi(app, user_db)

    post_db = PostDB(db)
    PostApi(app, post_db)
