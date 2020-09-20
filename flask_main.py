__author__ = "chris_daigle"
from flask import Flask, render_template
import statics
app = Flask(__name__)

post = statics.questions


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/exam")
def questions():
    return render_template('questions.html', posts=post, title='Exam')


if __name__ == '__main__':
    app.run(debug=True)
