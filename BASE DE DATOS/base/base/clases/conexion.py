import pymysql # type: ignore

class Conexion:
    host = "localhost"
    user = "root"
    password = ""
    bd = "udh"

    def obtener_conexion(self):
        return pymysql.connect(host = self.host,
                               user=self.user,
                               password=self.password,
                               db=self.bd)