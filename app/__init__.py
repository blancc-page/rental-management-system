
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
  app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://xqaredwhzxthom:c823bd2709d5f755ced9339de04ea8cc661e7516a532addcb86047b9209a4afd@ec2-54-160-109-68.compute-1.amazonaws.com:5432/d75080m4h0j7nc"
  db.init_app(app)
  
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


