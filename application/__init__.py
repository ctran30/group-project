from flask import Flask #import flask to create object
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) #myFlaskObj has been created
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)    #create the db object represent the database
migrate = Migrate(app, db)  #create the migrate object
@app.before_first_request
def create_table():
    from application.models import User
    db.create_all()
from application import routes, models

