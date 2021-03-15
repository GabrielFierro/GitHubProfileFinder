from wtforms import Form
from wtforms import StringField


class InputForm(Form):
    username = StringField('username')
