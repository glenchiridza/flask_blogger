from flask import Flask, render_template

app = Flask(__name__)


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
