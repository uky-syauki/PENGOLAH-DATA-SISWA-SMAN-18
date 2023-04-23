import os
from app.models import Barang
import sqlite3

class Koneksi:
	def __init__(self):
		self.koneksi = sqlite3.connect("app.db","a")
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
