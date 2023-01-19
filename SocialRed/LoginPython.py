import funciones as funcion
import archivo as ar


contador_usuarios = 0
session_id = 0
# inicio
opcion = funcion.bienvenida()

while not opcion == 1 or 2:

    # login
    if opcion == 1:

        if contador_usuarios > 0:
            correo_login, clave_login = funcion.pedir_datos()

            if correo_login in correos.values() and clave_login in claves.values():
                id1 = funcion.validar_id(correos, correo_login)
                id2 = funcion.validar_id(claves, clave_login)

                # Ventana principal
                if id1 == id2:
                    print("Acceso concedido")
                    session_id = id2
                    print("\t Bienvenido ", nombres.get(session_id), "\n")
                    opcion_inicio = funcion.opciones_principales()

                    while not opcion_inicio == 1 or 2 or 3 or 4:

                        # Opciones del inicio
                        if opcion_inicio == 1:
                            publicacion = funcion.publicar()
                            datos_publicacion = funcion.guardar_publicacion(nombres.get(session_id),
                                                                            publicacion, session_id)
                            lista_publicaciones = funcion.almacenar_publicacion(datos_publicacion)
                            print(lista_publicaciones)

                        elif opcion_inicio == 2:
                            print("2")

                        elif opcion_inicio == 3:
                            print("3")

                        elif opcion_inicio == 4:
                            print("Sesion cerrada correctamente!")
                            opcion = funcion.bienvenida()
                            break

                        else:
                            print("Digite una opcion correcta")
                            opcion_inicio = funcion.opciones_principales()

                else:
                    print("Correo o clave equivocada")
                    opcion = funcion.bienvenida()

            else:
                print("Correo o clave equivocadas")
                opcion = funcion.bienvenida()

        else:
            print("No hay ninguna cuenta creada")
            opcion = funcion.bienvenida()

    # registro
    elif opcion == 2:
        nombre, correo, clave = funcion.registro()

        if contador_usuarios > 0:

            if nombre in correos.values() or clave in claves.values():
                print("Ya existe este correo o clave")
                opcion = funcion.bienvenida()

            else:
                contador_usuarios += 1
                nombres, correos, claves = funcion.almacenamiento(nombres, correos, claves,
                                                                  nombre, correo, clave, contador_usuarios)

        else:
            contador_usuarios = 1
            nombres, correos, claves = funcion.guardar_registro(nombre, correo, clave, contador_usuarios)
        funcion.presentar(nombres, correos, claves)
        opcion = funcion.bienvenida()

    else:
        print("Digite una opcion correcta")
        opcion = funcion.bienvenida()
