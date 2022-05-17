from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
  firstname = StringField('First Name',validators=[DataRequired()])
  middlename = StringField('Middle Name')
  lastname = StringField('Last Name',validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired()])
  phonenumber = StringField('Phone Number',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired(),EqualTo('password_confirm',message='Password did not match')])
  password_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
  submit = SubmitField('Register')
  
  def validate_email(self,email_field):
    if User.query.filter_by(email=email_field.data).first():
      raise ValidationError('Account Exists')
    
class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  remember = BooleanField('Remember')
  submit = SubmitField('Login')
    
  
