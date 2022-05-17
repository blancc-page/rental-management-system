import os

class Config:
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:dclxvi@localhost/propertydb'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}