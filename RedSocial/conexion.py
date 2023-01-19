#Imporatcion Del Moduolo
import mysql.connector
 
#Creando el Objeto de Conexion
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "27866",
    database = "RedSocial"
)
 
cursor = mydb.cursor()


commit =  mydb.commit()

'''


'''

