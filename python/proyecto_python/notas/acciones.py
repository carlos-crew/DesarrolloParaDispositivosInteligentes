import notas
import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Introdusca el titulo de la nota: ")
        descripcion = input("Escribe el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()


        if guardar[0] >= 1:
                print(f"\n Perfecto ! Has guardado nota: {nota.titulo} ")
        else:
            print(f"\n NO se guardo tu nota, Intentalo mas tarde: {usuario[1]}")

    

    def mostrar(self, usuario):
        print(f"\n{usuario[1]}!!! Esats son tus notas: ") 

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

            #print(notas)

        for nota in notas:
            print("\n**************************")
            print(notas[2])
            print(notas[3])
            print("\n**************************")

        
        def borrar(self, usuario):
            print(f"\n{usuario[1]}!!! Borrar tus notas")

            titulo = input("Introduce titulo a la nota a borrar : ")
            nota = modelo.Nota(usuario[0], titulo)
            eliminar = nota.eliminar()

            if eliminar >= 1:
                print(f"Se borro tu nota: {nota.titulo}")

            else:
                print("No se borro la nota, preube mas tarde..")







        
