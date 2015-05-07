#Settings for Flask-WTF
WTF_CSRF_ENABLED = True #activates cross-site request forgery prevention
SECRET_KEY = 'you-will-never-guess' #creates token used to validate form

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#path of database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# Where SQLAlchemy-migrate data files stored
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
