'''
Main app entry point for development.
'''

from app import create_app


if __name__ == '__main__':
    app = create_app(__name__, 'app/dev_config.py')
    app.run()
