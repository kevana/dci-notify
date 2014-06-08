'''
Initialize the database for app.
Destroys all existing tables and creates schema based on SQLAlchemy
models.
'''


from app import create_app


if __name__ == '__main__':
    app = create_app(__name__, 'app/dev_config.py')

    db = app.extensions['sqlalchemy'].db
    with app.test_request_context():
        db.drop_all()
        db.create_all()
