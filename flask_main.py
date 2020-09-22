__author__ = "chris_daigle"
from flask import Flask, render_template, url_for, request
from forms import RegistrationForm, LoginForm
import statics
app = Flask(__name__)

app.config['SECRET_KEY'] = '49cd36e39f29b74c70077a555d57a02c'

post = statics.questions


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/exam")
def questions():
    return render_template('questions.html', posts=post, title='Exam')


@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    print("I received %s" % str(data))

    # do some database stuff

    return {"message": "OK"}, 200


if __name__ == '__main__':
    app.run(debug=True)
