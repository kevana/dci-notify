'''
Functions for app.
'''


from app.models import db, User
from app.sms import send_sms
from random import randint


def add_user(carrier, phone_number):
    '''Add a new user to the database and send a confirmation code.'''

    if User.query.get(phone_number):
        return False

    confirm_code = randint(10000, 99999)
    user = User(carrier, phone_number, confirm_code)

    db.session.add(user)
    db.session.commit()

    msg = 'Your confirmation number is: ' + str(confirm_code)
    send_sms(user.carrier, user.phone_number, msg)
    return True


def confirm_user(phone_number):
    '''Confirm a new user owns this phone number.'''
    user = User.query.get(phone_number)
    user.confirm_code = None
    user.confirmed = True
    db.session.commit()


def send_scores(scores):
    '''Send scores to registered users.'''
    users = User.query.filter(confirmed=True)
    for user in users:
        send_sms(user.carrier, user.number, 'Broadcast Message')
    pass
