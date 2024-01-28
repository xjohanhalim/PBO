from db import DBConnection as mydb

class Matakuliah:

    def __init__(self):
        self.__id = None
        self.__kode_mk = None
        self.__nama_mk = None
        self.__sks = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def kode_mk(self):
        return self.__kode_mk

    @kode_mk.setter
    def kode_mk(self, value):
        self.__kode_mk = value

    @property
    def nama_mk(self):
        return self.__nama_mk

    @property
    def sks(self):
        return self.__sks

    @nama_mk.setter
    def nama_mk(self, value):
        self.__nama_mk = value

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kode_mk, self.__nama_mk, self.__sks)
        sql = "INSERT INTO matakuliah (kode_mk, nama_mk, sks) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected


    def update(self, id):
        self.conn = mydb()
        val = (self.__kode_mk, self.__nama_mk, self.__sks, id)
        sql = "UPDATE matakuliah SET kode_mk = %s, nama_mk = %s, sks = %s WHERE id = %s" 
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM matakuliah WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        self.__kode_mk = self.result[1]
        self.__nama_mk = self.result[2]
        self.__sks = self.result[3]
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result

# Example Usage
A = Matakuliah()
B = A.getAllData()
print(B)

