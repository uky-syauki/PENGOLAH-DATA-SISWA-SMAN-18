from app.models import Barang, Terjual
from datetime import datetime


class TERJUAL:
	def __init__(self):
		self.allTerjual = Terjual.query.all()
	def data_on_date(self,tanggal=None):
		print("Test")
		hasil = 0
		if tanggal is None:
			tanggal = datetime.utcnow().strftime("%d-%m-%y")
		for isi in self.allTerjual:
			if isi.timestamp.strftime("%d-%m-%y") == tanggal:
				hasil += 1
		return hasil
	def bulan_sekarang(self):
		hasil = [[],[]]
		tanggal = datetime.utcnow().strftime("%m-%y")
		for i in range(1,31):
			if i < 10:
				forTanggal = f'0{i}-'+tanggal
			else:
				forTanggal = f'{i}-'+tanggal
			hasil[0].append(forTanggal)
			hasil[1].append(self.data_on_date(forTanggal))
		return hasil
	def bulan(self,bulan=None, tahun=None):
		hasil = [[],[]]
		if bulan is None:
			bulan = datetime.utcnow().strftime("-%m")
			if tahun is None:
				tahun = datetime.utcnow().strftime("-%y")
		for i in range(1,31):
			if i < 10:
				tanggal = f'0{i}'
			else:
				tanggal = f'{i}'
			hasil[0].append(tanggal+bulan+tahun)
			hasil[1].append(self.data_on_date(tanggal+bulan+tahun))
		return hasil, tanggal+bulan+tahun
