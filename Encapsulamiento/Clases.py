class Alumno:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def get_edad(self):
        return self.__edad
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
        
    def get_matricula(self):
        return self.__matricula
    
    def to_string(self):
        return "Nombre: " + self.__nombre + ", Edad: " + str(self.__edad) + ", Matrícula: " + self.__matricula
    
    def obtener_promedio(self, calificaciones):
        return sum(calificaciones) / len(calificaciones)
    
    def es_mayor_edad(self):
        if self.__edad >= 18:
            return True
        return False
    
    def asistir_clase(self):
        return "El alumno " + self.__nombre + " está asistiendo a clase."
    
    def entregar_tarea(self, nombre_tarea):
        return "El alumno " + self.__nombre + " ha entregado la tarea " + nombre_tarea + "."


class Auto:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        
    def setMarca(self, marca):
        self.__marca = marca
        
    def setModelo(self, modelo):
        self.__modelo = modelo
        
    def setAño(self, año):
        self.__año = año
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getAño(self):
        return self.__año
    
    def arrancar(self):
        return "El auto está arrancando."
    
    def acelerar(self):
        return "El auto está acelerando."
    
    def frenar(self):
        return "El auto está frenando."
    
    def apagar(self):
        return "El auto está apagado."

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def setCargo(self, cargo):
        self.__cargo = cargo
        
    def setSalario(self, salario):
        self.__salario = salario
        
    def getNombre(self):
        return self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSalario(self):
        return self.__salario
    
    def trabajar(self):
        return "El empleado está trabajando."
    
    def descansar(self):
        return "El empleado está descansando."
    
    def cobrar(self):
        return "El empleado ha cobrado su salario."


class Persona:
    def __init__(self, nombre, edad, genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setEdad(self, edad):
        self.__edad = edad
        
    def getEdad(self):
        return self.__edad
    
    def setGenero(self, genero):
        self.__genero = genero
        
    def getGenero(self):
        return self.__genero
    
    def caminar(self):
        return f"{self.__nombre} está caminando"
    
    def hablar(self, mensaje):
        return f"{self.__nombre} dice: {mensaje}"
    
    def dormir(self):
        return f"{self.__nombre} está durmiendo"
    
    def comer(self, alimento):
        return f"{self.__nombre} está comiendo {alimento}"

class Computadora:
    def __init__(self, marca, procesador, memoria, almacenamiento, sistema_operativo):
        self.__marca = marca
        self.__procesador = procesador
        self.__memoria = memoria
        self.__almacenamiento = almacenamiento
        self.__sistema_operativo = sistema_operativo
        self.__encendida = False

    def encender(self):
        if not self.__encendida:
            self.__encendida = True
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya se encuentra encendida.")

    def apagar(self):
        if self.__encendida:
            self.__encendida = False
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya se encuentra apagada.")

    def reiniciar(self):
        if self.__encendida:
            self.__encendida = False
            print("La computadora se está reiniciando...")
            self.__encendida = True
            print("La computadora se ha reiniciado.")
        else:
            print("La computadora debe estar encendida para reiniciar.")

    def instalar_programa(self, programa):
        if self.__encendida:
            print(f"Se está instalando {programa} en la computadora...")
            print(f"{programa} ha sido instalado correctamente.")
        else:
            print("La computadora debe estar encendida para instalar un programa.")

    def desinstalar_programa(self, programa):
        if self.__encendida:
            print(f"Se está desinstalando {programa} de la computadora...")
            print(f"{programa} ha sido desinstalado correctamente.")
        else:
            print("La computadora debe estar encendida para desinstalar un programa.")

    def ver_especificaciones(self):
        print(f"Marca: {self.__marca}")
        print(f"Procesador: {self.__procesador}")
        print(f"Memoria: {self.__memoria} GB")
        print(f"Almacenamiento: {self.__almacenamiento} GB")
        print(f"Sistema operativo: {self.__sistema_operativo}")
        print(f"Encendida: {'Sí' if self.__encendida else 'No'}")

    def actualizar_sistema_operativo(self, nuevo_sistema_operativo):
        if self.__encendida:
            print(f"Se está actualizando el sistema operativo: %s" % self.__encendida)
