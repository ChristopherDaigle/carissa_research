__author__ = "chris_daigle"
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return '<h1>Psychology Exam</h1>'


@app.route("/about")
def about():
    return "<h1>Home Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
