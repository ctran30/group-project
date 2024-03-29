from application import db
from datetime import datetime
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin #authenticated
from application import login   #loader function


class User(UserMixin, db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique = True)
    email = db.Column(db.String(128), index=True, unique = True)
    password_hash= db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
       return f'<user:{self.username}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamps = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
       return f'<post: {self.body}>'




@login.user_loader  #flask login user loader function
def load_user(id):  #database load string id
    return User.query.get(int(id))  #get string id and convert it to integer
