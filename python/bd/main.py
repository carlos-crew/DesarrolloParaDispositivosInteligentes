import mysql.connector

#Realizar conexion a la base de datos
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "capp_python"

)

#Ver si la conexion ha sido correcta
#print(database)

#Crear la base de datos
cursor = database.cursor(buffered=True)
#cursor.execute("CREATE DATABASE capp_python")
""" cursor.execute("CREATE DATABASE IF NOT EXISTS japs_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
 """

#Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

#incertar datos en un tabla
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 1850.00)")

coches = [
    ('Seat','Ibiza', 5000.00),
    ('Reanul','Clio', 15000.00),
    ('Citroen','Saxo', 2000.00),
    ('Mercedes','Clase C', 35000.00)
]
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
database.commit()

#Consulta a la tabla - select
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca ='Seat'")

result = cursor.fetchall()
print("----- Todos mis coches -----")

for coche in result:
    print(coche[1], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#Borrar un registro
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()

print(cursor.rowcount, "borrados!!!")

#Actualizar datos de un registro
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit()
print(cursor.rowcount, "Actualizados")


print("Carlos Antonio Peralta Perez", "9A", "Desarrollo para dispositivos inteligentes", "27/05/2022")
