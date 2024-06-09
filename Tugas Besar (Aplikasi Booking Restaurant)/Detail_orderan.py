
# filename : Detail_orderan.py
from db import DBConnection as mydb
class Detail_orderan:
    def __init__(self):
        self.__id=None
        self.__kode=None
        self.__no_meja=None
        self.__kode_order=None
        self.__qty=None
        self.__harga=None
        self.__subtotal=None
        
        self.conn = None
        self.affected = None
        self.result = None
        
    @property
    def id(self):
        return self.__id
    @property
    def kode(self):
        return self.__kode
        
    @kode.setter
    def kode(self, value):
        self.__kode = value
    @property
    def no_meja(self):
        return self.__no_meja
        
    @no_meja.setter
    def no_meja(self, value):
        self.__no_meja = value
    @property
    def kode_order(self):
        return self.__kode_order
        
    @kode_order.setter
    def kode_order(self, value):
        self.__kode_order = value
    @property
    def qty(self):
        return self.__qty
        
    @qty.setter
    def qty(self, value):
        self.__qty = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    @property
    def subtotal(self):
        return self.__subtotal
        
    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__kode,self.__no_meja,self.__kode_order,self.__qty,self.__harga,self.__subtotal)
        sql="INSERT INTO Detail_orderan (kode,no_meja,kode_order,qty,harga,subtotal) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    
    def update(self, id):
        self.conn = mydb()
        val = (self.__kode,self.__no_meja,self.__kode_order,self.__qty,self.__harga,self.__subtotal, id)
        sql="UPDATE detail_orderan SET kode = %s,no_meja = %s,kode_order = %s,qty = %s,harga = %s,subtotal = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    
    def updateByKODE(self, kode):
        self.conn = mydb()
        val = (self.__no_meja,self.__kode_order,self.__qty,self.__harga,self.__subtotal, kode)
        sql="UPDATE detail_orderan SET no_meja = %s,kode_order = %s,qty = %s,harga = %s,subtotal = %s WHERE kode=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM detail_orderan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def deleteByKODE(self, kode):
        self.conn = mydb()
        sql="DELETE FROM detail_orderan WHERE kode='" + str(kode) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM detail_orderan WHERE id='" + str(id) + "'"
        
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__kode = self.result[1]
        self.__no_meja = self.result[2]
        self.__kode_order = self.result[3]
        self.__qty = self.result[4]
        self.__harga = self.result[5]
        self.__subtotal = self.result[6]
        self.conn.disconnect
        return self.result
    
    def getByKODE(self, kode):
        a=str(kode)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM detail_orderan WHERE kode='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__kode = self.result[1]
           self.__no_meja = self.result[2]
           self.__kode_order = self.result[3]
           self.__qty = self.result[4]
           self.__harga = self.result[5]
           self.__subtotal = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__kode = ''
           self.__no_meja = ''
           self.__kode_order = ''
           self.__qty = ''
           self.__harga = ''
           self.__subtotal = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    
    def getAllData(self, nomor):
        # id, kode_order, nama_orderan, harga, qty, subtotal
        self.conn = mydb()
        sql="SELECT a.id, a.kode_order, b.nama_orderan, CONCAT(FORMAT(a.harga, 2), '') AS harga, a.qty, CONCAT(FORMAT(a.subtotal, 2), '') AS subtotal FROM detail_orderan AS a JOIN orderan AS b ON a.kode_order = b.kode_order WHERE a.no_meja = '" + nomor + "'"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,no_meja FROM detail_orderan"
        self.result = self.conn.findAll(sql)
        return self.result        
        