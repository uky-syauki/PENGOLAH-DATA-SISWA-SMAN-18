from app import app,db
from app.models import User, Terjual, Barang


class Table:
	def __init__(self,table):
		self.table = table
		if self.table == Barang:
			pass
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
		return data
	def insert(self,sortBy):
		pass
