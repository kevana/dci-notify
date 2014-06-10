'''
Contains test configuration directives for Flask and its plugins
'''

# Flask.session, CSRF
SECRET_KEY = 'Shhhh, this is a secret'
CSRF_ENABLED = False

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/travis_ci_test'

# Flask-Mail
MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'noreply@example.com'
MAIL_PASSWORD = 'examplePassword'
MAIL_DEFAULT_SENDER = 'noreply@example.com'

# administrator list
ADMINS = ['admin@example.com']
LOGGING_SENDER = 'server-error@example.com'
LOGGING_DISABLE = True

MAIL_SUPPRESS_SEND = True