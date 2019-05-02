from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,URL, ValidationError, Length

class LoginForm(FlaskForm):
	username = StringField('username',validators = [DataRequired()])
	password = PasswordField('password',validators = [DataRequired()])
	submit = SubmitField('submit')

class RegistrationForm(LoginForm):
	submit = SubmitField('register')
	pass


class CreateOrganizationForm(FlaskForm):
	name = StringField('name',validators=[DataRequired()])
	website = StringField('website',validators=[DataRequired()])
	mission= StringField('mission',validators=[DataRequired()])
	submit = SubmitField('CreateOrg')
	