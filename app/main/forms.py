from flask_wtf import FlaskForm 
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import *



class UpdateProfile(FlaskForm):
  firstname = StringField('First Name',validators=[DataRequired()])
  phonenumber = StringField('Phone Number',validators=[DataRequired()])
  biography = TextAreaField('About you',validators=[DataRequired()])
  submit = SubmitField('Submit')
  
TYPE = [('Land', 'Land'), ('Building', 'Building'), ('Business', 'Business')]
class AddPropertyForm(FlaskForm):
  property_type = SelectField('Type',choices=TYPE,validators=[DataRequired()])
  property_name = StringField('Name',validators=[DataRequired()])
  property_location = StringField('Location',validators=[DataRequired()])
  property_value = StringField('Value',validators=[DataRequired()])
  property_rooms = StringField('Rooms')
  submit = SubmitField('Add')

