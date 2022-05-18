from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import *



class UpdateProfile(FlaskForm):
  firstname = StringField('First Name',validators=[DataRequired()])
  phonenumber = StringField('Phone Number',validators=[DataRequired()])
  biography = TextAreaField('Aboout you',validators=[DataRequired()])
  submit = SubmitField('Submit')