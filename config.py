import os

class Config:
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
  pass

class TestConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}