# *-* coding=utf-8 *-*
from flask import (
                    Flask,
                    render_template,
                    request, url_for,
                    abort,
                    redirect,
                    session
                )
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
import config
from debug import *
from datetime import date
import json

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)

# helpMe(db)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(125), nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    password = db.Column(db.String(125), nullable=False)
    delete_flag = db.Column(db.Integer, default=0, doc='0:undelete, 1:deleted')
    create_date = db.Column(db.DateTime, default=func.now())
    update_date = db.Column(db.DateTime, nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=func.now())
    update_date = db.Column(db.DateTime, nullable=False)

class Article_user_relation(db.Model):
    __tablename__ = 'article_user_relation';
    article_user_relation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    article_id = db.Column(db.Integer, nullable=False)
db.create_all()

def md5(str):
    import hashlib
    return hashlib.md5(str).hexdigest()

def hash_sha1(str):
    import hashlib
    return hashlib.sha1(str).hexdigest()

def date():
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

admin = User(username = 'sangyufeiwan', email = '541885781@qq.com', password = hash_sha1(md5('123456')), update_date = date())
# db.session.add(admin)
# db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    page_title = 'login'
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if (email != '' and password != ''):
            user = User.query.filter_by(password = hash_sha1(md5(password))).filter_by(email = email).first()
            if user:
                session['current_user'] = user.username
                return redirect(url_for('top'))
            else:
                form_error = 'email or password error'
        else:
            form_error = 'email and password requied'

    return render_template('login.html', **locals())

@app.route('/top')
def top():
    if session['current_user'] == False:
        return redirect(url_for('login'))
    else:
        username = session['current_user']

    return render_template('top.html', username = username)

@app.route('/registe', methods = ['GET', 'POST'])
def registe():
    page_title = 'register'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        passconf = request.form.get('passconf')
        email = request.form.get('email')
        if (username != '' and password != '' and passconf != '' and email != ''):
            if password == passconf:
                pass
                user = User(username = username, email = email, password = hash_sha1(md5(password)), update_date = date())
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('registe_complete'))
            else:
                form_error =  'password not match passconf'
        else:
            form_error = 'username and password and passconf requied'

    return render_template('registe.html', **locals())

@app.route('/registe_complete')
def registe_complete():
    return render_template('registe_complete.html', page_title = 'registe')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
