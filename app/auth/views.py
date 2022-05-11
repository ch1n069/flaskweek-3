# from flask import render_template,redirect,url_for,abort,flash
# from app.main import main
# from flask_login import login_required


# from app.auth.forms import RegistrationForm, LoginForm  


# #Views go here
# @main.route('/')

# def index():


#     '''The home page of the application'''

    



#     return render_template('index.html')


# @main.route('/register' , methods=['GET','POST'])

# def register():
    
#     forms = RegistrationForm()

#     if forms.validate_on_submit():
#         flash(f'Account created  for {forms.username.data} proceed to login!!','success')
#         return redirect(url_for('main.login'))

#     return render_template('register.html', title='Register', forms=forms)
    

# @main.route('/login', methods=['GET', 'POST'])

# def login():
    
#     forms = LoginForm()
#     if forms.validate_on_submit():
#         if forms.email.data == forms.email.data and forms.password.data == '1234':
#             flash('you have been logged in ', 'success')
#             return redirect(url_for('main.index'))
#         else:
#             flash('login unsuccesfull', 'danger')



#     return render_template('login.html', title='login', forms=forms)
