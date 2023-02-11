from abc import ABC, abstractmethod

class Celular(ABC):
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def llamar(self, numero):
        pass

    @abstractmethod
    def enviar_mensaje(self, numero, mensaje):
        pass

    @abstractmethod
    def instalar_aplicacion(self, nombre_aplicacion):
        pass

    @abstractmethod
    def desinstalar_aplicacion(self, nombre_aplicacion):
        pass


class Router(ABC):
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def conectar_dispositivo(self, dispositivo):
        pass

    @abstractmethod
    def desconectar_dispositivo(self, dispositivo):
        pass

    @abstractmethod
    def configurar_red(self, nombre_red, contrasena):
        pass

    @abstractmethod
    def reiniciar(self):
        pass



class Camioneta(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def acelerar(self, velocidad):
        pass

    @abstractmethod
    def frenar(self):
        pass

    @abstractmethod
    def cambiar_marcha(self, marcha):
        pass

    @abstractmethod
    def cargar_equipaje(self, peso_equipaje):
        pass

    @abstractmethod
    def descargar_equipaje(self, peso_equipaje):
        pass

    @abstractmethod
    def encender_luces(self, estado):
        pass

class Internet(ABC):
    def __init__(self, proveedor, velocidad):
        self.proveedor = proveedor
        self.velocidad = velocidad

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @abstractmethod
    def obtener_direccion_IP(self):
        pass

    @abstractmethod
    def abrir_pagina_web(self, url):
        pass

    @abstractmethod
    def descargar_archivo(self, url):
        pass

    @abstractmethod
    def subir_archivo(self, archivo):
        pass

    @abstractmethod
    def enviar_correo_electronico(self, destinatario, asunto, mensaje):
        pass

    @abstractmethod
    def realizar_llamada_internet(self, destinatario):
        pass

class Producto(ABC):
    @abstractmethod
    def actualizar_stock(self, stock):
        pass
    @abstractmethod
    def aplicar_descuento(self, descuento):
        pass

class Destornillador(Producto):

        def __init__(self, descripcion, precio, stock):
            self.descripcion = descripcion
            self.precio = precio

            self.stock = stock
    
        def actualizar_stock(self, stock):
            self.stock = stock
       
        def aplicar_descuento(self, descuento):
            descuento = (100 - descuento) * 0.01 
            self.precio = self.precio * descuento
        def mostrar_datos(self):
            print("Producto:", self.descripcion)
            print("Precio:", self.precio)
            print("Stock:", self.stock)