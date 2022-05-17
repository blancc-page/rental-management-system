import os

class Config:
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  SECRET_KEY = 'property'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/propertydb'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = 'property'

class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://collo:1234@localhost/propertydb'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}