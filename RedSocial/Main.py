import fuccion as fun
import archivo as ar


contador_usuarios = 0
session_id = 0
# inicio

opcion = fun.bienvenida()
while not opcion == 1 or 2:

    # login
    if opcion == 1:
        
        id,user = fun.login()
        if  id >= 1:
            opciones = fun.Windox(user=user)
            
            if opciones == 1:
                fun.Publicar(id=id)
                opciones = fun.Windox(user=user)
            if opciones == 2:
                fun.Ver(id=id)
                opciones = fun.Windox(user=user)
            if opciones == 3:
                fun.EditUser(id=id)
                opciones = fun.Windox(user=user)
            if opciones == 4:
                opcion = 0
        else:
            opcion = 0

    elif opcion == 2:
        fun.Guardar_Usuario()
        opcion = fun.bienvenida()
    else:
    
        opcion = fun.bienvenida()
            