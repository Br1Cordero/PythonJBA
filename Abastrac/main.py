import Clases  as c
from abc import ABC, abstractmethod

cam = c.Camioneta (modelo= 'POER 4x4', año= 2021)

cam.encender()
cam.cambiar_marcha(marcha=5)
cam.acelerar(velocidad=150)
cam.frenar()