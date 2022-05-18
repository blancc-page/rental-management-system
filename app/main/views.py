from flask import render_template,abort,redirect,url_for
from . import main
from ..models import *
from .. import db
from .forms import UpdateProfile




@main.route('/')
def index():
  return render_template('index.html')


@main.route('/user/<firstname>')
def profile(firstname):
  user = User.query.filter_by(firstname=firstname).first()
  if user is None:
    abort(404)
    
  return render_template('profile/profile.html', user=user)
  
  
@main.route('/user/<firstname>/update',methods = ['GET','POST'])
def update_profile(firstname):
    user = User.query.filter_by(firstname = firstname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
      
      # user.biography = form.biography.data
      # user.phonenumber = form.phonenumber.data
      user = User(firstname=form.firstname.data,biography=form.biography.data,phonenumber=form.phonenumber.data)

      db.session.add(user)
      db.session.commit()

      return redirect(url_for('.profile', firstname=user.firstname))

    return render_template('profile/update.html',form =form)
