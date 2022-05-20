import os

class Config:
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  SECRET_KEY = 'property'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/propertydb'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'property'
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  DATABASE_URL="postgresql://eamvujmgmwjvxz:283e508ab9d77949f23009cafe38285920d6c0220d2975b17f56b18c11b7b1bc@ec2-34-201-95-176.compute-1.amazonaws.com:5432/d6bvv8hvt30f8e"
class TestConfig(Config):
  pass

class DevConfig(Config):
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/propertydb'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}