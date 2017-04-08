import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  def __init__(self):
    pass

  SECRET_KEY = os.environ.get('SECRET_KEY') or 'SOmething sweetish'
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = True

  @staticmethod
  def init(app):
    pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
  TESTING =True
  SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
 SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URL') or \
                            'sqlite:///' + os.path.join(basedir, 'data-production.sqlite')

class HerokuConfig(ProductionConfig):
  @classmethod
  def init_app(cls, app):
    ProductionConfig.init_app(app)
    
    import logging
    from logging.handlers import SysLogHandler
    syslog_handler  = SysLogHandler()
    syslog_handler.setLevel(logging.WARNING)
    app.logger.addHandler(syslog_hander)


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig
}
