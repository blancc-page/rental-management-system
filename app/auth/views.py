from pickle import GET
from turtle import title
from flask import render_template, redirect, url_for, flash , request
from . import auth
from .. models import *
from .forms import RegistrationForm
from .. import db


@auth.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    title = 'Registration'
    return render_template('auth/register.html', form = form, title = title)