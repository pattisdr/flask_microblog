from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #app reads config.py file

from app import views
