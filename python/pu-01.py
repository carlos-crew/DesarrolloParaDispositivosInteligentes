# print("hahah")

# # Definir una Funcion 
# def muestrameNombre():
# print("Carlos")
# print("David")
# 
# Invocar la funcion 




# Ejemplo 2
# print("###### Ejemplo 2 ######" )


# nombre = "Carlos"
# cadena = ", es el contenido de la variable : nombre."

# def mostrarTuNombre(nombre,edad):
#  print("Tu nombre es: {nombre}, {cadena} ")
#  print("Tu nombre es: {nombre}")
#  if edad >= 18:
#      print("Eres mayor de edad.")
#  else:
#          print("Eres menor de edad.")


# nombre = input("Introduce tu nombre: ")
# edad = int (input("Introdece tu edad: "))
# mostrarTuNombre(nombre, edad)


# mostrarTuNombre("Carlos")
# mostrarTuNombre("Peralta")
# mostrarTuNombre("Perez")

#Ejemplo 3
# print("")
# print("###### Ejemplo 3: Funciones y Parametros ##########")

# def Tabla(numero):
#     print(f"Tabla de multiplicar del numero: {numero}")

#     for contador in range(11):
#         operacion = numero * contador
#         print(f"{numero} x {contador} = {operacion}"

# tabla(23)
# tabla(3)
# tabla(7)

# # Ejemplo 3.1
# print("----------------------------------------------")

# for numero_tabla in range(1,11):
#     tabla(numero_tabla)

# Ejemplo 4: Parametros opcionales

#print("###### Ejemplo 4: Parametros ##########")

from __future__ import division


def getEmpleado(nombre, dni= None):
    print("Empleado")
    print(f"Nombre: {nombre}" )
    print(f"DNI: {dni}" )

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Carlos Peralta ","1234")

# Ejemplo 5: Parametros opcionales y retura a devolver datos
#print("###### Ejemplo 5: Parametros ##########")

def saludame(nombre):
    saludo = f"Hola,saludos DDI - {nombre}"

    return saludo

print(saludame("Carlos Antonio")) 

#Ejemplo 6
# print("## Ejemplo 6 ###")

# def calculadora(numero1, numero2, basicas = False):

#     suma = numero1 + numero2
#     resta = numero1 - numero2
#     multi = numero1 * numero2
#     division = numero1 / numero2

#     cadena = ""
# if basicas != False:
#       cadena += "suma:" + str(suma)
#       cadena += ""
#       cadena += "resta:" +str(resta)
# else:
#       cadena += "multiplicacion:" +str(multi)
#       cadena += ""
#       cadena += "division:" +str(division)

#      return cadena

# print(calculadora(5, 5,True))
    

