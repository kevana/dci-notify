'''
Views for app.
'''

from flask import Blueprint, redirect, render_template, url_for
from app.forms import ConfirmForm, SignupForm
from app.functions import add_user, confirm_user
from app.models import User

main = Blueprint('main', __name__, template_folder='app/templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    #TODO: Add chosen to carrier list
    form = SignupForm()
    registered = False
    if form.validate_on_submit():
        carrier = form.carrier.data
        phone_number = int(form.phone_number.data)
        print(phone_number)
        if add_user(carrier, phone_number):
            return redirect(url_for('main.confirm',
                                    carrier=carrier,
                                    number=phone_number))
    try:
        phone_number = int(form.phone_number.data)
    except:
        phone_number = None

    if phone_number and User.query.get(phone_number):
        registered = True
    return render_template('index.html', form=form, registered=registered)


@main.route('/confirm/<carrier>/<number>', methods=['GET', 'POST'])
def confirm(carrier, number):
    #TODO: Implement resend feature
    form = ConfirmForm()
    if form.validate_on_submit():
        phone_number = int(form.phone_number.data)
        confirm_user(phone_number)
        return redirect(url_for('main.done'))
    #TODO: Handle malformed inputs
    form.phone_number.data = number
    form.carrier.data = carrier
    return render_template('confirm.html',
                           form=form,
                           carrier=carrier,
                           number=number)


@main.route('/done')
def done():
    return render_template('done.html')


@main.route('/scores/new')
def new_scores():
    #TODO: Implement auth first
    return 'Unimplemented'
    data = get_json()
    try:
        obj = json.loads(data)
    except ValueError:
        return 'Bad Request'
    if obj:
        send_scores(obj)
