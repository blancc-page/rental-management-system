from flask import render_template,abort,redirect,url_for,flash,request
from . import main
from ..models import *
from .. import db
from .forms import UpdateProfile,AddPropertyForm
from flask_login import current_user




@main.route('/')
def index():
  return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
      abort(404)
      
    return render_template('profile/profile.html', user=user)

# @main.route('/user/<int:id>',methods = ['GET','POST'])
# def update_profile(id):
#   form = UpdateProfile()
#   name_to_update = User.query.filter_by(user_id=id)
#   if request.method == "POST":
#     name_to_update.firstname = form.firstname.data
#     name_to_update.phonenumber =  form.phonenumber.data
#     name_to_update.biography =  form.biography.data
#     try:
#       db.session.commit()
#       flash('Updated successfully')
#       return render_template('profile/profile.html',id=id)
#     except:
#       flash('Not Updated')
#       return render_template('profile/update.html',form =form,name_to_update=name_to_update)
    
#   else:
#     return render_template('profile/update.html',form =form,name_to_update=name_to_update)
  
  
@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
      
        user.biography = form.biography.data
        user.phonenumber = form.phonenumber.data
        user.firstname = form.firstname.data
        # user = User(firstname=form.firstname.data,biography=form.biography.data,phonenumber=form.phonenumber.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html',form =form)
  
@main.route('/add_property',methods=['GET','POST'])
def add_property():
  form = AddPropertyForm()
  properties = Property.query.all()
  if form.validate_on_submit():
      property_type = form.property_type.data
      property_name = form.property_name.data
      property_location = form.property_location.data
      property_value = form.property_value.data
      property_rooms = form.property_rooms.data
      # user_id = current_user
      # user_id=current_user._get_current_object().id
      new_property_object = Property(property_type=property_type,property_name=property_name,property_value=property_value,property_rooms=property_rooms,property_location=property_location)
      
      new_property_object.save_property()
      flash('Added property')
      return render_template('properties.html',properties=properties)
  return render_template('add_property.html',form=form)
    

  