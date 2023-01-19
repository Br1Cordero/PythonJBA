from os import system
import archivo as ar

# Funcion de bienvenida
def bienvenida():
    #  system("cls")
    print("\r BIENVENIDO A  ESTA RED SOCIAL")
    print('''Inicie sesion o registrese
    1. Iniciar sesion
    2. Registrarse''')
    opcion = int(input("Digite una de las opciones: "))
    return opcion


# Funciones de inicio de sesion
def pedir_datos():
    system("cls")
    print("Ingrese su correo y clave")
    correo = input("Ingrese su correo: ")
    clave = input("Ingrese su clave: ")
    return correo, clave


def verificar_datos(correo_noVerificado, clave_noVerificada, correo, clave):
    if correo_noVerificado != correo:
        verificar = 0
    else:
        if clave_noVerificada != clave:
            verificar = 0
        else:
            verificar = 1
    return verificar


def validar_id(diccionario, dato):
    lista_id = list(diccionario.keys())
    lista_datos = list(diccionario.values())

    valor = lista_datos.index(dato)
    return lista_id[valor]


# Funciones de registro
def registro():
    #  system("cls")
    print("Registre sus datos")
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electronico: ")
    clave = input("Ingrese su clave: ")
    return nombre, correo, clave


def guardar_registro(nombre, correo, clave, contador_usuarios):
    lista_nombre = {
        contador_usuarios: nombre
    }
    lista_correo = {
        contador_usuarios: correo
    }
    lista_clave = {
        contador_usuarios: clave
    }
    num = contador_usuarios 
    lista = (str(num)+'  '+nombre +'  ' +correo +'  '+ clave)
    ar.ModificarArchivo(lista)
    print("Datos guardados correctamente")
    return nombre, lista_correo, lista_clave


def almacenamiento(lista_nombre, lista_correo, lista_clave, nombre, correo, clave, contador_usuarios):
    lista_nombre[contador_usuarios] = nombre
    lista_correo[contador_usuarios] = correo
    lista_clave[contador_usuarios] = clave
    
 
    return lista_nombre, lista_correo, lista_clave


# Funciones del inicio
def opciones_principales():
    print("Que quieres hacer hoy?")
    print("1. Publicar")
    print("2. Ver publicaciones")
    print("3. Editar informacion")
    print("4. Cerrar sesion")
    opcion = int(input("Digite una de las opciones: "))
    return opcion


def publicar():
    #  system("cls")
    print("Que estas pensando hoy?\n")
    publicacion = input(">>> ")
    return publicacion


def guardar_publicacion(nombre, publicacion, id_publicacion):
    lista_info = (nombre, publicacion, id_publicacion)
    return lista_info


def almacenar_publicacion(publicacion):
    lista_publicaciones = [publicacion]
    return lista_publicaciones


# Funciones de prueba
def presentar(nombres, correos, claves):
    #  system("cls")

    print(nombres, "\n") 
    print(correos, "\n")
    print(claves, "\n")
