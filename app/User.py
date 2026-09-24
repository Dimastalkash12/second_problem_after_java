from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from db import Users,db

class User(UserMixin):

    def __init__(self,userId):
        self.userId=userId
        self.user=db.session.execute(
            db.select(Users).filter_by(id=userId)
        ).scalar_one_or_none()


    @staticmethod
    def get(login):
        user=db.session.execute(db.select(Users).filter_by(login=login)).scalar_one_or_none()
        if user is not None:
            return User(user.id)
        return None
    @staticmethod
    def auth(login,password):
        user = db.session.execute(db.select(Users).filter_by(login=login)).scalar_one_or_none()

        if user is not None and check_password_hash(user.password,password):
            return User(user.id)
        return None

    def get_id(self):
        return str(self.userId)
    def isAdmin(self):
        return self.user.rights=='admin'

generate_password_hash('54321')