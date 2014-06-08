'''
Main app entry point for uWSGI in production.
'''


from app import create_app

app = create_app(__name__, 'prd_config.py')

if __name__ == '__main__':
    print('Warning: Running production config as __main__.')
