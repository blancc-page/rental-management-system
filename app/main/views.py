from crypt import methods
from flask import render_template,abort,redirect,url_for,flash,request
from . import main
from ..models import *
from .. import db,photos
from .forms import UpdateProfile,AddPropertyForm
from flask_login import current_user




@main.route('/')
def index():
  return render_template('index.html')

 
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    properties = Property.query.filter_by(user_id=current_user._get_current_object().id ).all()
    properties = Property.query.filter_by(property_type='land').all()
    if user is None:
      abort(404)
      
    return render_template('profile/profile.html', user=user,properties=properties)
  
@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    updateform = UpdateProfile()
    if updateform.validate_on_submit():
      
        user.biography = updateform.biography.data
        user.phonenumber = updateform.phonenumber.data
        user.firstname = updateform.firstname.data
        # user = User(firstname=form.firstname.data,biography=form.biography.data,phonenumber=form.phonenumber.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html',updateform =updateform)
  
@main.route('/add_property',methods=['GET','POST'])
def add_property():
  form = AddPropertyForm()
  properties = Property.query.filter_by(user_id =current_user._get_current_object().id ).all()
  lands = Property.query.filter_by(property_type='Lands').all()
  if form.validate_on_submit():
      property_type = form.property_type.data
      property_name = form.property_name.data
      property_location = form.property_location.data
      property_value = form.property_value.data
      property_rooms = form.property_rooms.data
      user_id = current_user
      new_property_object = Property(property_type=property_type,user_id=current_user._get_current_object().id,property_name=property_name,property_value=property_value,property_rooms=property_rooms,property_location=property_location)
      
      new_property_object.save_property()
      flash('Added property')
      
      return render_template('profile/profile.html',properties=properties,user=user_id,lands=lands)
  return render_template('add_property.html',form=form)
    
@main.route('/property_details<pname>',methods=['GET','POST'])
def property_details(pname):
  property = Property.query.filter_by(property_name=pname).all()
  return render_template('properties.html',property=property)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_picture = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

  