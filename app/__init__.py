'''
Simple app to send a text message.
'''

from flask import Flask
from flask.ext.mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')

mail = Mail(app)


@app.route('/')
def index():

    msg = Message('Subject', recipients=['3205835412@vtext.com'])
    msg.body = 'Test Message'
    mail.send(msg)
    return 'Message sent'
