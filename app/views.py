
# the sys method is to help us go into the folder of auth using the prepend method

from flask import render_template,redirect,url_for,abort,flash,request
from app.main import main
from app.auth.forms import RegistrationForm, LoginForm  
from app.models import User
from app import db, bcrypt
from flask_login import login_user, current_user, logout_user,login_required




#views

@main.route('/')
def index():

    '''The home page of the application'''



    return render_template('index.html')


@main.route('/register' , methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    forms = RegistrationForm()

    if forms.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')

        user  = User(username=forms.username.data, email=forms.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created !!','success')
        return redirect(url_for('main.login')) 

    return render_template('register.html', title='Register', forms=forms)
    

@main.route('/login', methods=['GET', 'POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    
    
    forms = LoginForm()
    if forms.validate_on_submit():
        user = User.query.filter_by(email=forms.email.data).first()
        print(forms.password.data) 
        if user and bcrypt.check_password_hash(user.password,forms.password.data):
        # if user.password == forms.password.data:
            login_user(user,remember=forms.remember.data)
            next_page = request.args.get('next')
            login_user(user)
            #terniary conditonal
            return  redirect(next_page) if next_page is not None else redirect(url_for('main.index'))
        else:
            flash('Please input valid credentials   ', 'danger')
        return redirect(url_for('main.login'))
       



    return render_template('login.html', title='login', forms=forms)

@main.route('/logout')
def logout():

    logout_user()
    return redirect(url_for('main.index'))


    
@main.route('/account')
@login_required
def account():


    return render_template('account.html', title='account')


