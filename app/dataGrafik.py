from app.models import Barang, Terjual

class DataGrafik:
	def __init__(self):
		self.data_barang = Barang.query.all()
		self.data_terjual = Terjual.query.all()
	def Rp(self,uang):
		uang = str(uang)
		hasil = ""
		c = 0
		for huruf in uang[::-1]:
			if c == 3:
				hasil += "."
				c = 0
			hasil += huruf
			c += 1
		return hasil[::-1]
	def forKeuangan(self,bln=None):
		hasil = {}
		total = ["Total",0,0,0]
		if bln is not None:
			if len(str(bln)) == 1:
				bln = "0"+str(bln)
		for isi in self.data_terjual:
			if isi.timestamp.strftime("%m") == bln or bln is None:
				pass
			else:
				continue
			if isi.kode_barang in hasil.keys():
				hasil[isi.kode_barang][1] += 1
				pilih = self.data_barang[0].query.filter(Barang.kode_barang==isi.kode_barang).first()
				hasil[isi.kode_barang][2] += pilih.harga_modal
				hasil[isi.kode_barang][3] += pilih.harga_jual-pilih.harga_modal
			else:
				bungkus = []
				bungkus.append(isi.kode_barang)
				bungkus.append(1)
				pilih = self.data_barang[0].query.filter(Barang.kode_barang==isi.kode_barang).first()
				bungkus.append(pilih.harga_modal)
				bungkus.append(pilih.harga_jual-pilih.harga_modal)
				hasil[isi.kode_barang] = bungkus
			total[1] += 1
			total[2] += pilih.harga_modal
			total[3] += pilih.harga_jual-pilih.harga_modal
			print(hasil)
			print(total)

		kembalikan = []
		hasil["total"] = total
		for isi in hasil.values():
			nama = isi[0]
			banyak = isi[1]
			modal = "Rp "+self.Rp(isi[2])
			untung = "Rp "+self.Rp(isi[3])
			kembalikan.append([nama,banyak,modal,untung])
		return kembalikan
