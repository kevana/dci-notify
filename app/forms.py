'''
Forms for AppName
'''

from flask.ext.wtf import Form
from wtforms import HiddenField, IntegerField, SelectField, TextField
from wtforms.validators import Regexp, Required, ValidationError

from app.sms import carriers
from app.models import User


carrier_tuples = [(key, carriers[key]['name']) for key in carriers.keys()]
carrier_tuples.sort(key=lambda tup: tup[0])


class SignupForm(Form):
    '''Form for initial signup.'''
    carrier = SelectField('Carrier', choices=carrier_tuples)
    phone_number = TextField('Phone Number', [Required()])

    def validate_phone_number(form, field):
        val = field.data
        val = form.num_filter(val)
        field.data = val
        if len(val) != 10:
            raise ValidationError('Invalid input.')
        if User.query.get(int(val)):
            raise ValidationError('Number already registered.')

    def num_filter(self, seq):
        '''Remove all non-numeric characters from seq'''
        seq_type = type(seq)
        return seq_type().join(filter(seq_type.isdigit, seq))


class ConfirmForm(Form):
    '''Form for confirming signup.'''
    carrier = HiddenField('Carrier', [Required()])
    phone_number = HiddenField('Phone Number', [Required()])
    confirm_code = IntegerField('Confirmation Code', [Required()])

    def validate_confirm_code(form, field):
        try:
            phone_number = int(form.phone_number.data)
        except:
            phone_number = None
            raise ValidationError('Invalid phone number.')

        user = User.query.get(phone_number)
        if not user or user.confirm_code != field.data:
            raise ValidationError('Incorrect code.')
