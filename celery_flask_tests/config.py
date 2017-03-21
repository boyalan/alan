#coding=utf-8
class Config(object):
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/sqls?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@192.168.75.128/test'
    # 该配置为True,则每次请求结束都会自动commit数据库的变动
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'Config':Config,

    'default': DevelopmentConfig
}
