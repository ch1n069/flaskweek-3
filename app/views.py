
# the sys method is to help us go into the folder of auth using the prepend method

from flask import render_template,redirect,url_for,abort
from app import app
from app.auth.forms import RegistrationForm, LoginForm  





#views

@app.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')


@app.route('/register' , methods=['GET','POST'])
def register():
    if form.validate_on
    forms = RegistrationForm()
    return render_template('register.html', title='Register', forms=forms)
    

@app.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html', title='login', forms=forms)
