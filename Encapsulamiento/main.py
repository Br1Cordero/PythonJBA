import Clases as c

compu =  c.Computadora(marca = 'Dell', procesador = 'Intel Core 7', memoria = 16, almacenamiento =500 , sistema_operativo = 'Windoxs' )

compu.apagar()
compu.actualizar_sistema_operativo(nuevo_sistema_operativo='Linux')
compu.ver_especificaciones()
compu.instalar_programa(programa='Office 365')
compu.desinstalar_programa(programa= 'Excel')

print ("\n")

al = c.Alumno(nombre = 'Bruno', edad = 20, matricula = ' TENDENCIAS  DE PROGRAMACION')

al.asistir_clase()
al.entregar_tarea(nombre_tarea='Codigos en Python')
al.es_mayor_edad()
