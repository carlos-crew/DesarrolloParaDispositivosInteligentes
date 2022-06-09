from sqlite3 import Cursor, connect
from typing_extensions import Self
from unittest import result
import datetime
import hashlib # Cifrar contraseña en python
import usuarios.conexion as conexion


# llamar la clase conectar
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Crifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)


        try:
           cursor.execute(sql, usuario)
           database.commit()
           result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result 

    def identificar(self):
        # Login de usuarios
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # cifrado contraseña login
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (Self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result


        

print("Carlos Antonio Peralta Perez", "9A", "Desarrollo para dispositivos inteligentes", "30/05/2022")
