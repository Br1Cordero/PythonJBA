import conexion as con
import archivo as ar
from os import system

def bienvenida():
    system("cls")
    print("\r BIENVENIDO A  ESTA RED SOCIAL")
    print('''Inicie sesion o registrese
    1. Iniciar sesion
    2. Registrarse''')
    opcion = int(input("Digite una de las opciones: "))
    return opcion

def Guardar_Usuario():
    system('cls')    
    print("\t *** Registre sus datos ***")
    Apellidos = input ("\r Ingrese sus Apellidos: ")
    Nombres = input ("\r Ingrese sus Nombres: ")
    Genero = input ("\r Ingrese su Genero (M/F): ")
    Email = input ("\r Ingrese su Email: ")
    Password = input ("\r Ingrese su  Contraseña: ")
    sql = "INSERT INTO tb_cliente (Apellidos, Nombres, Genero, Email, Password) VALUES ('"+str(Apellidos)+"', '"+str(Nombres)+"', '"+str(Genero)+"', '"+str(Email)+"', '"+str(Password)+"');"
    con.cursor.execute(sql)
    con.mydb.commit()
    text = str(Apellidos)+"' '"+str(Nombres)+"'  '"+str(Genero)+"' '"+str(Email)+"' '"+str(Password)+"'"
    ar.ModificarArchivo(text)
    
    return Apellidos,Nombres,Genero,Email,Password
    

def login():
    system('cls')    
    print("\t***  LOGIN ***")
    Email = input ("\r Ingrese su Email: ")
    Password = input ("\r Ingrese su  Contraseña: ")
    con.cursor.execute("SELECT COUNT(*), Nombres,Id FROM tb_cliente where email = '"+ Email+"' and password = '"+ Password+"'")
    
    for x in con.cursor:
        list =[x]
    count = list[0][0]
    user = list[0][1]
    id = list[0][2]
    if not count ==1:
        print ("Error en los datos ingresados")
        id = 0
    return id,user

def Windox(user):
    system('cls')
    print("\t *** Bienvennido  "+user+"   ***")
    print("""Que quieres hacer hoy?
    1. Publicar
    2. Ver publicaciones
    3. Editar informacion
    4. Cerrar sesion""")
    
    opcion = int(input("Digite una de las opciones: "))
    return opcion

def Publicar(id):
    system('cls')    
    print("\t *** DINOS QUE VAS HA PUBLICAR  ***")
    titulo = input("Ingrese el titulo:  ")
    contenido = input("Ingrese el contenido de su publicacion:  ")
    
    con.cursor.execute("call redsocial.InsertPublicacion('"+ str(id)+"', '"+titulo+"', '"+contenido+"');")
    con.mydb.commit()


    print("Guardado con exito 😎😎")

def Ver(id):
    system('cls')    
    con.cursor.execute("SELECT p.Titulo, p.Contenido, p.F_Creacion FROM tb_publicacion as tb, tb_cliente as c, tb_publicacion_cuerpo as p  where usuario = c.Id and publicacion = p.Id and tb.Usuario = '"+str(id)+"';")
    
    for x in con.cursor:
        print (x)

def EditUser(id):
    system('cls')    
    print("\t *** Actualize sus sus datos ***")
    Apellidos = input ("\r Ingrese sus Apellidos: ")
    Nombres = input ("\r Ingrese sus Nombres: ")
    Password = input ("\r Ingrese su  Contraseña: ")
    
    con.cursor.execute("UPDATE tb_cliente SET Apellidos='"+Apellidos+"', Nombres = '"+Nombres+"', Password = '"+Password+"', F_Modificacion = curdate() WHERE Id = '"+str(id)+"';")
    con.mydb.commit()


    print ("Datos actualizados")

