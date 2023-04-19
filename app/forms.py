from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	username = StringField("Nama Pengguna", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Kata Sandi", validators=[DataRequired()])
	password2 = PasswordField("Ulangi Kata Sandi", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField('Daftar')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError("Nama Pengguna telah ada, tolong gunakan yang lain.")

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError("Email telah ada, tolong gunakan email yang lain.")

class TransaksiForm(FlaskForm):
	kode_barang = StringField("Kode Barang", validators=[DataRequired()])
	submit = SubmitField("Kirim")
