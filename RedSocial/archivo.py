import os

def CrearArchivo():
    archivo  = open('./user.user', 'w')
    archivo.close()

def ModificarArchivo(text):
    print(__file__)
    archivo  = open('./user.user', 'a')
    archivo.write('\n'+ text )
    archivo.close()


def leer_archivo():
    archivo = open('./user.user')

    for inline in archivo:
        print ( inline, end="")
    archivo.close()


CrearArchivo()




