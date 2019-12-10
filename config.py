import os   #import os library(the location of database)
basedir = os.path.abspath(os.path.dirname(__name__)) #directory

class Config():
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') #set sqlalchemy where to set database
    SQLALCHEMY_TRACK_MODIFICATIONS = False