# Importar Modulo
import sqlite3

# Conexion 
conexion = sqlite3.connect('pruebas.db')

# Cursor para crear una tabla
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT"+
"titulo VARCHAR(255), "+
"descripcion TEXT, "+
"precio INT(255)"+
")")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros de una sola instruccion 
productos = [
    ("Ordenador portatil", "Buena calidad", 750),
    ("Telefono movil", "Xaommi 7", 160),
    ("Placa base XT2345", "Para Windows", 90),
    ("Tablet ", "Samsung", 250)
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

# Update 
cursor.execute("UPDATE productos SET precio=110 WHERE precio=90")

# Listar datos 
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
# print(cursor)
productos = cursor.fetchall()
# print(productos)

# for producto in productos:
#     print(producto)

print("\n")
for producto in productos:
    print("Titulo: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchall()
print("\n")
print(producto)



# Cerrar la conexion 
conexion.close


print("Carlos Antonio Peralta Perez", "9A", "Desarrollo para dispositivos inteligentes", "26/05/2022")
