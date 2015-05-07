from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Dawn'}
    posts = [
        {
            'author': {'nickname': 'James'},
            'body': 'Graduating May 15th!'
        },
        {
            'author': {'nickname': 'Eric'},
            'body': 'Got 17 hours of sleep!'

        }

    ]
    return render_template('index.html', title = 'Home', user = user, posts=posts)
