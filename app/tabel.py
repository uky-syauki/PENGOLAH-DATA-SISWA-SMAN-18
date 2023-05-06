from app import app,db
from app.models import User, Terjual, Barang
from datetime import datetime


class Table:
	def __init__(self,table):
		self.table = table
		if self.table == Barang:
			pass
	def TableTrx(self):
		trxd = Terjual.query.all()
		data = []
		panjang = conter = len(trxd)
		for i in range(panjang):
			conter += 1
			bungkus = []
			bungkus.append(trxd[panjang-conter].timestamp.strftime("%d-%m-%y, %H:%M"))
			bungkus.append(trxd[panjang-conter].kode_barang)
			fromBarang = Barang.query.filter_by(kode_barang=trxd[panjang-conter].kode_barang).first()
			bungkus.append(fromBarang.nama_barang)
			bungkus.append(fromBarang.harga_jual)
			bungkus.append(fromBarang.tersedia)
			try:
				fromUser = User.query.filter_by(id=trxd[panjang-conter].user_id).first()
				bungkus.append(fromUser.username)
			except:
				bungkus.append("Tidak diketahui!")
			data.append(bungkus)
		return data
	def TableBarang(self):
		barang = Barang.query.all()
		for i in range(len(barang)):
			for k in range(len(barang)):
				if barang[i].tersedia < barang[k].tersedia:
					barang[i], barang[k] = barang[k], barang[i]
		daftar = []
		i = 0
		for isi in barang:
			i += 1
			bungkus = []
			bungkus.append(i)
			bungkus.append(isi.kode_barang)
			bungkus.append(isi.nama_barang)
			bungkus.append(isi.harga_jual)
			bungkus.append(isi.tersedia)
			daftar.append(bungkus)
		return daftar
	def select(self,field=None):
		data = []
		if field is None:
			query = db.select(self.table)
		else:
			query = db.select(self.table).where(self.table.kode_barang==field)
		getData = db.session.execute(query)
		for row in getData:
			sdat = []
			for kolom in row:
				if self.table == Barang:
					sdat.append(kolom.id)
					sdat.append(kolom.kode_barang)
					sdat.append(kolom.nama_barang)
					sdat.append(kolom.harga_jual)
					sdat.append(kolom.tersedia)
				elif self.table == Terjual:
					sdat.append(kolom.timestamp.strftime("%d/%m/%y, %H:%M"))
					sdat.append(kolom.kode_barang)
					dataBarang = Barang.query.filter_by(kode_barang=kolom.kode_barang).first()
					sdat.append(dataBarang.nama_barang)
					sdat.append(dataBarang.harga_jual)
					sdat.append(dataBarang.tersedia)
					try:
						adminnya = User.query.filter_by(id=kolom.user_id).first()
						sdat.append(adminnya.username)
					except:
						sdat.append("Tidak diketahui")
			data.append(sdat)
#		newData = []
#		panjang = conter = len(data)
#		for i in range(len(data)):
#			conter += 1
#			newData.append(data[panjang-conter])
		return data
	def update(self,kolom,nilai):
		sebelum = Table(Barang).select(kolom)
		sesudah = sebelum[0][-1] + nilai
		query = db.update(self.table).where(self.table.kode_barang==kolom).values(tersedia=sesudah)
		db.session.execute(query)
		db.session.commit()


class forGrafik:
	def __init__(self):
		self.all_barang = {}
		self.getData()
	def getData(self):
		allBarang = [[],[]]
		data = Terjual.query.all()
		for isi in data:
			if isi.kode_barang in self.all_barang:
				self.all_barang[isi.kode_barang] += 1
			else:
				self.all_barang[isi.kode_barang] = 1
		for k in self.all_barang.keys():
			allBarang[0].append(k)
			allBarang[1].append(self.all_barang[k])
		return allBarang
#	def terjual_this_day(self):
#		hasil = []
#		allTerjual = Terjual.query.all()
#		tgl_now = datetime.utcnow()
#		tgl_now = tgl_now.strftime("%d")
#		for isi in allTerjual:
#			if isi.timestamp.strftime("%d") == tgl_now:
#				hasil.append(isi.kode_barang)
#		return hasi

class HitungTerjual:
	def __init__(self):
		self.allData = Terjual.query.all()
	def banyak_on_date(self,tgl=None):
		hasil = 0
		if tgl is None:
			tgl = datetime.utcnow().strftime("%d")
		else:
			tgl = tgl
		for isi in self.allData:
			if isi.timestamp.strftime("%d") == tgl:
				hasil += 1
		return hasil
	def full_date(self):
		hasil = [[],[]]
		tgl = 0
		for i in range(30):
			tgl += 1
			hasil[1].append(self.banyak_on_date(str(tgl)))
			hasil[0].append(str(tgl))
		return hasil

