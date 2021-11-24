from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddBlackCard(FlaskForm):
    list_item = TextAreaField('Item:', validators=[DataRequired()])
    submit = SubmitField('Add')

class AddWhiteCard(FlaskForm):
    list_item = TextAreaField('Item:', validators=[DataRequired()])
    submit = SubmitField('Add')