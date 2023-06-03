from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, TransaksiForm, UpdateForm, StatistikForm, UpdateForm2, FormBulan
from app.models import User, Barang, Terjual
from app.buat import Buat, DataGrafik
from app.tabel import Table

app.app_context().push()

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
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
	form = FormBulan()
	DataGrafik("3")
	user = {'username':'Ahmad syauki'}
#	allTerjual = Terjual.query.all()
	data = Table(Terjual).TableTrx()
#	for isi in allTerjual:
#		bungkus = []
#		bungkus.append(isi.timestamp.strftime("%H:%M %m-%d-%y"))
#		bungkus.append(isi.kode_barang)
#		try:
#			fromBarang = Barang.query.filter_by(kode_barang=isi.kode_barang).first()
#			bungkus.append(fromBarang.nama_barang)
#			bungkus.append(fromBarang.harga_jual)
#		except:
#			bungkus.append("None")
#			bungkus.append("None")
#		data.append(bungkus)
	if form.validate_on_submit():
		DataGrafik(form.bulan.data)
	return render_template('index.html', title='Halaman Utama', data=data, form=form)


@app.route("/user")
@login_required
def user():
	return "This User"


@app.route("/register", methods=['GET', 'POST'])
@login_required
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


@app.route('/transaksi', methods=['GET', 'POST'])
@login_required
def transaksi():
	data = Table(Terjual).TableTrx()
#	terjual_all = Terjual.query.all()
#	bnya = conter = len(terjual_all)
#	for i in range(bnya):
#		conter += 1
#		bungkus = []
#		bungkus.append(i+1)
#		bungkus.append(terjual_all[bnya-conter].timestamp.strftime("%H:%M %m-%d-%y"))
#		bungkus.append(terjual_all[bnya-conter].kode_barang)
#		try:
#			fromBarang = Barang.query.filter_by(kode_barang=terjual_all[bnya-conter].kode_barang).first()
#			bungkus.append(fromBarang.nama_barang)
#			bungkus.append(fromBarang.harga_jual)
#			bungkus.append(fromBarang.tersedia)
#		except:
#			bungkus.append("None")
#			bungkus.append("None")
#			bungkus.append("None")
#		data.append(bungkus)
	form = TransaksiForm()
	total_tr = len(data)
	Buat()
	if form.validate_on_submit():
		barang = Barang.query.filter_by(kode_barang=form.kode_barang.data).first()
		if barang is None:
			flash("Kode Barang tidak terdaftar!")
			return redirect(url_for("transaksi"))
		if barang.tersedia < 1:
			flash("Jumlah Barang Habis")
			return redirect(url_for("transaksi"))
		jual = Terjual(kode_barang=form.kode_barang.data,user_id=current_user.id)
		barang.tersedia = barang.tersedia - 1
		db.session.add(jual)
		db.session.add(barang)
		db.session.commit()
		return redirect(url_for('transaksi'))
	return render_template('transaksi.html', title="Transaksi", form=form, data=data, total_tr=total_tr)


@app.route('/update', methods=['GET', 'POST'])
@login_required
def update():
#	sample = Barang.query.all()
	daftar = Table(Barang).TableBarang()
#	for isi in sample:
#		aDaftar = []
#		aDaftar.append(isi.id)
#		aDaftar.append(isi.kode_barang)
#		aDaftar.append(isi.nama_barang)
#		aDaftar.append(isi.harga_jual)
#		aDaftar.append(isi.tersedia)
#		daftar.append(aDaftar)
	form = UpdateForm()
	form2 = UpdateForm2()
	if form.validate_on_submit():
		barang = Barang(kode_barang=form.kode_barang.data,nama_barang=form.nama_barang.data,harga_jual=form.harga_jual.data, harga_modal=form.harga_modal.data,tersedia=form.tersedia.data)
		db.session.add(barang)
		db.session.commit()
		return redirect(url_for("update"))
	elif form2.validate_on_submit():
		barang = Table(Barang)
		barang.update(form2.kode_barang2.data,form2.tambah_stok.data)
		return redirect(url_for("update"))
	return render_template('update.html', title="Update Barang", form=form, daftar=daftar, form2=form2)


@app.route('/statistik') 
@login_required
def statistik():
	return redirect( url_for("statistik"))


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))
