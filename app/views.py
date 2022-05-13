import os
# the sys method is to help us go into the folder of auth using the prepend method
import secrets
from app import main
from flask import render_template,redirect,url_for,abort,flash,request
from app.main import main
from app.auth.forms import RegistrationForm, LoginForm  , UpdateAccountForm , PostForm
from app.models import User , Pitch
from app import db, bcrypt
from flask_login import login_user, current_user, logout_user,login_required
# from app.email import mail_message




#views

@main.route('/')
def index():

    '''The home page of the application'''

    posts = Pitch.query.all()




    return render_template('index.html' , posts=posts )


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
        # mail_message("Welcome to pitch na sisi ","templates/email/welcome_user",user.email,user=user)
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


    
# def save_picture(forms_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(forms_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path,'static/profile_pics',picture_fn)
#     forms_picture.save(picture_path)


    return picture_fn



@main.route('/account',methods=['GET', 'POST'])
@login_required
def account():
    forms = UpdateAccountForm()
    # if forms.picture.data:
        # picture_file = save_picture(forms.picture.data)
        # current_user.image_file = picture_file
         






    if forms.validate_on_submit():
        current_user.username = forms.username.data
        current_user.email = forms.email.data
        db.session.commit()
        flash('Your account details were updated !', 'success')
        return redirect(url_for('main.account'))
    elif request.method == 'GET':
        forms.username.data = current_user.username
        forms.email.data = current_user.email



    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)


    return render_template('account.html', title='account', image_file=image_file, forms = forms)



@main.route("/post/new",methods=['GET', 'POST'])
@login_required
def new_post():
    forms = PostForm()

    if forms.validate_on_submit():
        post  = Pitch(title=forms.title.data, content=forms.content.data , category=forms.category.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('post was created successfully', 'success')
        return redirect(url_for('main.index'))



    return render_template('create_post.html', title='new post',forms = forms,legend='create new post ' )


@main.route("/post/<int:post_id>")
def post(post_id):
    post = Pitch.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Pitch.query.get_or_404(post_id)
    if post.author != current_user:
        abort (403)
    forms = PostForm()
   
    if forms.validate_on_submit():
        post.title = forms.title.data
        post.content = forms.content.data
        db.session.commit()


        flash('Your post has been updated', 'success')
        return redirect(url_for('main.post',post_id=post.id))
    elif request.method == 'GET':

        forms.title.data = post.title
        forms.content.data = post.content
    
    return render_template('create_post.html', title='Update post',forms=forms, legend='update post ')
    



@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Pitch.query.get_or_404(post_id)
    if post.author != current_user:
        abort (403)

    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", 'success')
    return redirect(url_for('index'))