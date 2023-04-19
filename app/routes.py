from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, TransaksiForm
from app.models import User




@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Nama pengguna atau Password salah!')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)


@app.route('/')
@app.route('/index')
@login_required
def index():
	user = {'username':'Ahmad syauki'}
	data =[
		{
			'barang':'Telkomsel 6 GB',
			'harga':30000
		},
		{
			'barang':'Telkomsel Sakti',
			'harga':45000
		}
	]
	return render_template('index.html', title='Halaman Utama', data=data)


@app.route("/user")
def user():
	return "This User"


@app.route("/register", methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Selamat, sekarang kamu terdaftar")
		return redirect(url_for('login'))
	return render_template('register.html', title="Daftar", form=form)


@app.route('/transaksi')
def transaksi():
	form = TransaksiForm()
	return render_template('transaksi.html', title="Transaksi", form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
