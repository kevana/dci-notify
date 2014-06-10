'''
Simple app to send a text message.
'''

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
import json

import os
basedir = os.path.abspath(os.path.dirname(__file__))

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

    if not app.debug:
        import logging
        from logging import Formatter
        from logging.handlers import SMTPHandler, RotatingFileHandler
        mail_handler = SMTPHandler(mailhost=app.config['MAIL_SERVER'],
                                   fromaddr=app.config['LOGGING_SENDER'],
                                   toaddrs=app.config['ADMINS'],
                                   subject='dci-notify Server Error',
                                   credentials=(app.config['MAIL_USERNAME'],
                                                app.config['MAIL_PASSWORD']))

        file_handler = RotatingFileHandler(filename=os.path.join(basedir,
                                                                 'app.log'),
                                           maxBytes=1048756,
                                           backupCount=5)

        mail_handler.setLevel(logging.ERROR)
        file_handler.setLevel(logging.WARNING)
        mail_handler.setFormatter(Formatter('''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s

            Message:

            %(message)s
        '''))

        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))
        app.logger.addHandler(mail_handler)
        app.logger.addHandler(file_handler)

    return app
