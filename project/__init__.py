import os

from flask import Flask
from flask_celeryext import FlaskCeleryExt

from project.celery_utils import make_celery

ext_celery = FlaskCeleryExt(create_celery_app=make_celery)


def create_app():
    app = Flask(__name__)

    with app.app_context():
        app_settings = os.environ.get(
            "APP_SETTINGS", "project.config.DevelopmentConfig"
        )
        app.config.from_object(app_settings)

        ext_celery.init_app(app)  # celery configuration

        from project.apis import api

        api.init_app(app)

        @app.shell_context_processor
        def ctx():  # pragma: no cover
            return {"app": app}

    return app
