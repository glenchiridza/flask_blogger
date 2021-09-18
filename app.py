from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30),nullable=False, default="N/A")
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return "Blog Post"+ str(self.id)


@app.route('/')
def index():
    return render_template('index.html')


all_posts = [
    {
        "title": "Post 1",
        "content": "This is content of post1"
    },
    {
        "title": "Post 2",
        "author":"Glenc",
        "content": "This is content of post2"
    }
]


@app.route('/posts')
def posts():
    return render_template('posts.html',posts=all_posts)


@app.route('/home/<string:name>')
def hello(name):
    return "hello world " + name


@app.route('/onlyget', methods=['GET'])
def get_only():
    return "you can only get this web page"


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='127.0.0.1')
