'''
Contains test configuration directives for Flask and its plugins
'''

# Flask.session, CSRF
SECRET_KEY = 'Shhhh, this is a secret'
CSRF_ENABLED = False

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/travis_ci_test'

# administrator list
ADMINS = ['admin@example.com']
LOGGING_SENDER = 'server-error@example.com'


MAIL_SUPPRESS_SEND = True
