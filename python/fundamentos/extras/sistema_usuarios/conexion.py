import mysql.connector
# Es una libreria que conecta mysql con python

class Conexion:
    @staticmethod
    def conectar():
        conexion = mysql.connector.connect(
            host="localhost", # se conecta
            user="root", #usuario
            password="1234", #contraseña del usuario de nosotros 
            database="usuarios_db" #que tipo debase de datos estamos utilizando
        )
        return conexion #retornar la bd (conexion)