# filename : Penyewa.py
from db import DBConnection as mydb
class Penyewa:
    def __init__(self):
        self.__no=None
        self.__no_meja=None
        self.__penyewa=None
        self.__tanggal=None
        self.__jam=None
        self.__jumlah_kursi=None
        self.__makanan=None
        self.__minuman=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def no(self):
        return self.__no
    @property
    def no_meja(self):
        return self.__no_meja
        
    @no_meja.setter
    def no_meja(self, value):
        self.__no_meja = value
    @property
    def penyewa(self):
        return self.__penyewa
        
    @penyewa.setter
    def penyewa(self, value):
        self.__penyewa = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def jam(self):
        return self.__jam
        
    @jam.setter
    def jam(self, value):
        self.__jam = value
    @property
    def jumlah_kursi(self):
        return self.__jumlah_kursi
        
    @jumlah_kursi.setter
    def jumlah_kursi(self, value):
        self.__jumlah_kursi = value
    @property
    def makanan(self):
        return self.__makanan
        
    @makanan.setter
    def makanan(self, value):
        self.__makanan = value
    @property
    def minuman(self):
        return self.__minuman
        
    @minuman.setter
    def minuman(self, value):
        self.__minuman = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__no_meja,self.__penyewa,self.__tanggal,self.__jam,self.__jumlah_kursi,self.__makanan,self.__minuman)
        sql="INSERT INTO Penyewa (no_meja,penyewa,tanggal,jam,jumlah_kursi,makanan,minuman) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__no_meja,self.__penyewa,self.__tanggal,self.__jam,self.__jumlah_kursi,self.__makanan,self.__minuman, id)
        sql="UPDATE penyewa SET no_meja = %s,penyewa = %s,tanggal = %s,jam = %s,jumlah_kursi = %s,makanan = %s,minuman = %s WHERE no=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNO_MEJA(self, no_meja):
        self.conn = mydb()
        val = (self.__penyewa,self.__tanggal,self.__jam,self.__jumlah_kursi,self.__makanan,self.__minuman, no_meja)
        sql="UPDATE penyewa SET penyewa = %s,tanggal = %s,jam = %s,jumlah_kursi = %s,makanan = %s,minuman = %s WHERE no_meja=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM penyewa WHERE no='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNO_MEJA(self, no_meja):
        self.conn = mydb()
        sql="DELETE FROM penyewa WHERE no_meja='" + str(no_meja) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM penyewa WHERE no='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__no = self.result[0]
        self.__no_meja = self.result[1]
        self.__penyewa = self.result[2]
        self.__tanggal = self.result[3]
        self.__jam = self.result[4]
        self.__jumlah_kursi = self.result[5]
        self.__makanan = self.result[6]
        self.__minuman = self.result[7]
        self.conn.disconnect
        return self.result
    def getByNO_MEJA(self, no_meja):
        a=str(no_meja)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM penyewa WHERE no_meja='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__no = self.result[0]
           self.__no_meja = self.result[1]
           self.__penyewa = self.result[2]
           self.__tanggal = self.result[3]
           self.__jam = self.result[4]
           self.__jumlah_kursi = self.result[5]
           self.__makanan = self.result[6]
           self.__minuman = self.result[7]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__no = ''
           self.__no_meja = ''
           self.__penyewa = ''
           self.__tanggal = ''
           self.__jam = ''
           self.__jumlah_kursi = ''
           self.__makanan = ''
           self.__minuman = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM penyewa"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,penyewa FROM penyewa"
        self.result = self.conn.findAll(sql)
        return self.result