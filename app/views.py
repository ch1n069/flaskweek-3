import sys

# the sys method is to help us go into the folder of auth using the prepend method

from flask import render_template,redirect,url_for,abort
from app import app
sys.path.append("/home/moringa/moringa_pre-prep/flask/pitch-app/app/auth")
from forms import RegistrationForm , LoginForm  





#views

@app.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')


@app.route('/register')
def register():
    forms = RegistrationForm()
    return render_template('register.html', title='Register', forms=forms)
    

@app.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html', title='login', forms=forms)
    