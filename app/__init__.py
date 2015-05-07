from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #app reads config.py file
db = SQLAlchemy(app) #creates db object that will be our database

from app import views, models
