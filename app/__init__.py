'''
Simple app to send a text message.
'''

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import json

from app.models import User


def create_app(name, config_filename):
    app = Flask(name,
                template_folder='app/templates',
                static_folder='app/static')
    app.config.from_pyfile(config_filename)

    from app.models import db
    db.init_app(app)
    db.app = app
    from app.sms import mail
    mail.init_app(app)
    mail.app = app

    from app.views import main
    app.register_blueprint(main)

    #TODO: Secure admin view
    admin = Admin()
    admin.init_app(app)
    admin.app = app
    admin.add_view(ModelView(User, db.session))

    #TODO: Add logging

    return app
