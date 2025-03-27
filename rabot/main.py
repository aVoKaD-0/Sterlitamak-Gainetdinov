import flask
from data import db_session
from data.works import Works
from flask import render_template

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/works')
def works():
    db_sess = db_session.create_session()
    works = db_sess.query(Works).all()
    return render_template('works.html', works=works)

def main():
    db_session.global_init("db/blogs.db")
    app.run()