from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import *
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,login_required,logout_user,current_user


@auth.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(firstname=form.firstname.data,username = form.username.data,lastname=form.lastname.data,email=form.email.data,phonenumber=form.phonenumber.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  title = 'Registration'
  return render_template('auth/register.html',form=form, title=title)

@auth.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  # properties = Property.query.filter_by(user_id=current_user._get_current_object().id ).all()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user,form.remember.data)
      return render_template('profile/profile.html',user=user)
    
    flash('Invalid username or password')
  title = 'Login'  
  return render_template('auth/login.html',title=title, form=form)
    
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))

