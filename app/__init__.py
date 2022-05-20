
from flask import Flask
import flask_sqlalchemy
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy




photos = UploadSet('photos',IMAGES)

bootstrap = Bootstrap()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
  
  app = Flask(__name__)
  
  #app configurations
  app.config.from_object(config_options[config_name])
 
  db.init_app(app)
  app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://eamvujmgmwjvxz:283e508ab9d77949f23009cafe38285920d6c0220d2975b17f56b18c11b7b1bc@ec2-34-201-95-176.compute-1.amazonaws.com:5432/d6bvv8hvt30f8e"
  
  #initialize flask extensions
  bootstrap.init_app(app)
  db.init_app(app) 
  login_manager.init_app(app) 

  
  #configure_uploadset
  configure_uploads(app,photos)
  
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix='/')
  
  
  #Register blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  
  
  
  return app


