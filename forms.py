from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email)


class ContactForm(Form):
    name = StringField(
        'Name',
        validators=[
            DataRequired()
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    message = TextAreaField(
        'Message',
        validators=[DataRequired()]
    )