import sqlite3

class DbSql:
	def __init__(self):
		self.conn = sqlite3.connect("../app.db")
		self.cursor = self.conn.cursor()
	def getList(self):
		query = f"SELECT kode_barang FROM barang"
		self.cursor.execute(query)
		return self.cursor.execute()

