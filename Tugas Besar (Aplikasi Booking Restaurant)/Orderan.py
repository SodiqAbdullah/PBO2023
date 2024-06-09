	# filename : Orderan.py
from db import DBConnection as mydb
class Orderan:
    def __init__(self):
        self.__id=None
        self.__kode_order=None
        self.__nama_orderan=None
        self.__harga=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def kode_order(self):
        return self.__kode_order
        
    @kode_order.setter
    def kode_order(self, value):
        self.__kode_order = value
    @property
    def nama_orderan(self):
        return self.__nama_orderan
        
    @nama_orderan.setter
    def nama_orderan(self, value):
        self.__nama_orderan = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_order,self.__nama_orderan,self.__harga)
        sql="INSERT INTO Orderan (kode_order,nama_orderan,harga) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_order,self.__nama_orderan,self.__harga, id)
        sql="UPDATE orderan SET kode_order = %s,nama_orderan = %s,harga = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByKODE_ORDER(self, kode_order):
        self.conn = mydb()
        val = (self.__nama_orderan,self.__harga, kode_order)
        sql="UPDATE orderan SET nama_orderan = %s,harga = %s WHERE kode_order=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM orderan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByKODE_ORDER(self, kode_order):
        self.conn = mydb()
        sql="DELETE FROM orderan WHERE kode_order='" + str(kode_order) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM orderan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode_order = self.result[1]
        self.__nama_orderan = self.result[2]
        self.__harga = self.result[3]
        self.conn.disconnect
        return self.result
    def getByKODE_ORDER(self, kode_order):
        a=str(kode_order)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM orderan WHERE kode_order='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode_order = self.result[1]
           self.__nama_orderan = self.result[2]
           self.__harga = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode_order = ''
           self.__nama_orderan = ''
           self.__harga = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM orderan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama_orderan FROM orderan"
        self.result = self.conn.findAll(sql)
        return self.result       