from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  __tablename__='users'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(30))
  lastname = db.Column(db.String(30))
  username = db.Column(db.String(255))
  email = db.Column(db.String(100),unique=True,index=True,nullable=False)
  phonenumber = db.Column(db.Integer())
  pass_secure = db.Column(db.String(255))
  profile_picture = db.Column(db.String(255))
  biography = db.Column(db.String(255))
  Properties = db.relationship('Property',backref='user',lazy = 'dynamic')
  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')
  
  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)
    
  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)
  
  def __repr__(self):
    return f'User {self.username}'
  
  
class Property(db.Model):
  __tablename__ = 'properties'
  id = db.Column(db.Integer(), primary_key=True)
  property_type = db.Column(db.String(255))
  property_name = db.Column(db.String(255))
  property_location = db.Column(db.String(255))
  property_value = db.Column(db.Integer)
  property_rooms = db.Column(db.Integer)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  
  
  def save_property(self):
    db.session.add(self)
    db.session.commit()
    
  @classmethod
  def get_property(cls,property_type):
    properties = Property.query.filter_by(property_type=property_type).all()
    return properties
  
  def __repr__(self):
    return f'Pitch {self.property}'
