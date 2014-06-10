'''
Main app entry point for uWSGI in production.
'''


from app import create_app

app = create_app(__name__, 'app/prd_config.py')

if __name__ == '__main__':
    print('Warning: Attempting to run production app as __main__.')
    app.run()
