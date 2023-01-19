import conexion as con
import archivo as ar
from os import system

def bienvenida():
    #  system("cls")
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
    con.cursor.execute("SELECT Email, Password FROM tb_cliente")
    while con.cursor.move_to_next():
        print(con.cursor[1])
    