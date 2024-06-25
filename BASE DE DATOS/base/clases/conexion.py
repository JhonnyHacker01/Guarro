import pymysql

class Conexion:
    def obtener_conexion():
        return pymysql.conect(host="localhost", 
                               user="root",
                               password="", 
                               db="udh")

