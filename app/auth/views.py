from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import *
from .forms import RegistrationForm,LoginForm
from .. import db


@auth.route('/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(firstname=form.firstname.data,middlename=form.middlename.data,lastname=form.lastname.data,email=form.email.data,phonenumber=form.phonenumber.data,password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
  title = 'Registration'
  return render_template('auth/register.html',form=form, title=title)

@auth.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      return redirect(request.args.get('next') or url_for('main.index'))
    
    flash('Invalid username or password')
  title = 'Login'  
  return render_template('auth/login.html', form=form,title=title)
    
