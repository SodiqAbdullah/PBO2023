# filename : Penyewa.py
from db import DBConnection as mydb
class Penyewa:
    def __init__(self):
        self.__id=None
        self.__no_meja=None
        self.__nama=None
        self.__jumlah_orang=None
        self.__tanggal=None
        self.__jam=None
        self.__total_bayar=None
        self.__lunas=None
        
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    @property
    def no_meja(self):
        return self.__no_meja
        
    @no_meja.setter
    def no_meja(self, value):
        self.__no_meja = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jumlah_orang(self):
        return self.__jumlah_orang
        
    @jumlah_orang.setter
    def jumlah_orang(self, value):
        self.__jumlah_orang = value
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
    def total_bayar(self):
        return self.__total_bayar
        
    @total_bayar.setter
    def total_bayar(self, value):
        self.__total_bayar = value
    @property
    def lunas(self):
        return self.__lunas
        
    @lunas.setter
    def lunas(self, value):
        self.__lunas = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__no_meja,self.__nama,self.__jumlah_orang,self.__tanggal,self.__jam,self.__total_bayar,self.__lunas)
        sql="INSERT INTO Penyewa (no_meja,nama,jumlah_orang,tanggal,jam,total_bayar,lunas) VALUES " + str(val)
        
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__no_meja,self.__nama,self.__jumlah_orang,self.__tanggal,self.__jam,self.__total_bayar,self.__lunas, id)
        sql="UPDATE penyewa SET no_meja = %s,nama = %s,jumlah_orang = %s,tanggal = %s,jam = %s,total_bayar = %s,lunas = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def updateByNO_MEJA(self, no_meja):
        self.conn = mydb()
        val = (self.__nama,self.__jumlah_orang,self.__tanggal,self.__jam,self.__total_bayar,self.__lunas, no_meja)
        sql="UPDATE penyewa SET nama = %s,jumlah_orang = %s,tanggal = %s,jam = %s,total_bayar = %s,lunas = %s WHERE no_meja=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    
    def updateTotalbayar(self, nominal, no_meja):
        self.conn = mydb()
        val = (nominal, no_meja)
        sql="UPDATE penyewa SET total_bayar = %s WHERE no_meja=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected

    def setLunas(self, no_meja):
        self.conn = mydb()
        val = (no_meja,)
        sql="UPDATE penyewa SET lunas = '1' WHERE no_meja=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM penyewa WHERE id='" + str(id) + "'"
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
        sql="SELECT * FROM penyewa WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__no_meja = self.result[1]
        self.__nama = self.result[2]
        self.__jumlah_orang = self.result[3]
        self.__tanggal = self.result[4]
        self.__jam = self.result[5]
        self.__total_bayar = self.result[6]
        self.__lunas = self.result[7]
        self.conn.disconnect
        return self.result
    
    def getTotalbayar(self, nomor):
        self.conn = mydb()
        sql="SELECT total_bayar FROM penyewa WHERE no_meja='" + str(nomor) + "'"
        self.result = self.conn.findOne(sql)
        self.__total_bayar = self.result[0]
        self.conn.disconnect
        return self.__total_bayar
    
    def getByNO_MEJA(self, no_meja):
        a=str(no_meja)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM penyewa WHERE no_meja='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__no_meja = self.result[1]
           self.__nama = self.result[2]
           self.__jumlah_orang = self.result[3]
           self.__tanggal = self.result[4]
           self.__jam = self.result[5]
           self.__total_bayar = self.result[6]
           self.__lunas = self.result[7]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__no_meja = ''
           self.__nama = ''
           self.__jumlah_orang = ''
           self.__tanggal = ''
           self.__jam = ''
           self.__total_bayar = ''
           self.__lunas = ''
        
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
        sql="SELECT id,nama FROM penyewa"
        self.result = self.conn.findAll(sql)
        return self.result