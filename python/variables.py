








# Variables globales

from turtle import st


frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres"

print(frase)

def holaMundo():
    frase = "Hola Mundo!!!!"
    print("Dentro de la Funcion")
    print(frase)

    year = 2022
    print(year)

    global website
    website = "www.uttehuacan.edu.mx/web"
    print("Dentro: ", website)

    return "Dato devuelto" + str(year)

print(holaMundo())
print("FUERA: ", website)
