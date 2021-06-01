from sqlalchemy.dialects.postgresql import UUID

from weekendinator import db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    id = db.Column(UUID, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    is_superadmin = db.Column(db.Boolean, default=False, nullable=False)


    def __repr__(self):
        return self.username

    def get_id(self):
        return self.id
