# coding=utf-8
from config import config
from flask import Flask
from celery import Celery
celery = Celery(__name__, broker=config['Config'].CELERY_BROKER_URL)


def create_app(config_name):
    app = Flask(__name__,
                template_folder='', #指定模板路径，可以是相对路径，也可以是绝对路径。
                # static_folder='static',
                )
    app.config.from_object(config[config_name])

    from celery_flask import celery_test
    app.register_blueprint(celery_test, url_prefix='/celery_test')
    celery.conf.update(app.config)

    return app
