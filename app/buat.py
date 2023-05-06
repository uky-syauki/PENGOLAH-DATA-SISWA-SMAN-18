import os
from app.models import Barang, Terjual
from app.tabel import HitungTerjual
import sqlite3
from datetime import datetime

class Koneksi:
	def __init__(self):
		self.koneksi = sqlite3.connect("mysite/app.db","a")
		self.cursor = self.koneksi.cursor()
	def getInfoTrx(self):
		self.cursor.execute("SELECT timestamp, terjual.kode_barang, nama_barang, harga_jual FROM terjual.kode_barang=barang.kode_barang")
		return self.cursor.fetchall()



class Buat:
	def __init__(self):
		if bool(os.system("cat mysite/app/static/data.json")):
			self.f = open("mysite/app/static/data.json","a")
			self.dsql = []
			for isi in Barang.query.all():
				self.dsql.append(isi.kode_barang)
			self.dsql = str(self.dsql)
			self.text = "data = {'kbarang':" + str(self.dsql) + "}"
			self.f.writelines(self.text)
#			print(self.txt)
			self.f.close()
		else:
			os.system("rm mysite/app/static/data.json")
			Buat()


class DataGrafik:
	def __init__(self):
		self.allData = Terjual.query.all()
		if bool(os.system("cat mysite/app/static/dataGrafig.json")):
			self.f = open("mysite/app/static/dataGrafig.json","a")
			self.getData, self.bln = self.full_date()
			self.f.writelines("GrafikData =" + str(self.getData))
			self.f.writelines(";\nbulan = ["+str(self.bln)+"]")
			self.f.close()
		else:
			os.system("rm mysite/app/static/dataGrafig.json")
			DataGrafik()
	def banyak_ondate(self, tgl = None):
		hasil = 0
		if tgl is None:
			tgl = datetime.utcnow().strftime("%d-%m")
		else:
			tgl = tgl
		for isi in self.allData:
			if isi.timestamp.strftime("%d-%m") == tgl:
				hasil += 1
		return hasil
	def full_date(self, bln=None):
		hasil = [[],[]]
		tgl = 0
		if bln is None:
			bln = datetime.utcnow().strftime("%m")
		else:
			bln = bln
			if type(bln) == int:
				bln = str(bln)
		for i in range(30):
			tgl += 1
			if tgl < 10:
				hasil[1].append(self.banyak_ondate("0"+str(tgl)+"-"+bln))
			else:
				hasil[1].append(self.banyak_ondate(str(tgl)+"-"+bln))
			hasil[0].append(str(tgl))
		return hasil, bln
