from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired, Length ,   Email , EqualTo,ValidationError

from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('email', validators=[DataRequired(),Email()])

    password = PasswordField('password', validators=[DataRequired(),])

    confirm_password = PasswordField('confirm_password', validators=[DataRequired(),EqualTo('password')])



    submit  = SubmitField('signup')


    #check if username is taken
    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken please choose another one ')


    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That  email already exists ')



class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])


    password = PasswordField('password', validators=[DataRequired(),])


    remember = BooleanField('remember me')




    submit  = SubmitField('login')





