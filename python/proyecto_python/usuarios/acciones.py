import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):

        print("Se procedera a realizar tu registro en el sistema.....")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("¿Introduce tu email?:")
        password = input("¿Introduce tu contraseña?: ")

        # ***************************************
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente !!")
        # ***************************************

    def login(self):

        print("\nIdentificacion en el sistema...... ")


        try:
            email = input("Introduce tu correo... ")
            password = input("Introduce tu password... ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificador()

            if email == login[3]:
             print(f"Bienvenido {login[1]}, te az registrado {login[5]}")
             self.proximasAcciones(login)


        except Exception as e:
                # print(type(e))
                # print(type(e)._name_)
                print("Login incorrecto")

    def proximasAcciones(self,usuario):
        print("""
        
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar notas (mostrar)
            - Eliminar notas  (eliminar)
            - Salir        
        """)

        accion = input("¿Que quieres hacer ?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
           # print("Vamos a crear notas")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)


            self.proximasAcciones(usuario)
        elif accion == "mostrar":
          #  print("Vamos a mostrar")
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            #print("Vamos a eliminar")   
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario) 
        elif accion == "salir":    
            exit()
        #return None
