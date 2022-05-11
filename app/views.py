
# the sys method is to help us go into the folder of auth using the prepend method

from flask import render_template,redirect,url_for,abort,flash
from app.main import main
from app.auth.forms import RegistrationForm, LoginForm  
from app.models import User
from app import db




#views

@main.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')


@main.route('/register' , methods=['GET','POST'])
def register():
    forms = RegistrationForm()

    if forms.validate_on_submit():
        user  = User (username=forms.username.data, email=forms.email.data,password=forms.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created !!','success')
        return redirect(url_for('main.login'))

    return render_template('register.html', title='Register', forms=forms)
    

@main.route('/login', methods=['GET', 'POST'])
def login():
    
    forms = LoginForm()
    if forms.validate_on_submit():
       
        flash('you have been created ', 'success')
        return redirect(url_for('login'))
       



    return render_template('login.html', title='login', forms=forms)
