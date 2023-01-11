# Biblioteca grafica 
# pip install PyQt6

from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton,
QLineEdit, QPushButton, QMessageBox, QCheckBox)

from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtGui import QPalette, QFont, QPixmap
from PyQt6.QtCore import Qt

import sys

class Ventana(QWidget):

  def __init__(self):
    super().__init__()  
    self.inicializarUI()

  def inicializarUI(self):
    self.setGeometry(100,100,800,500)
    self.setWindowTitle('CONDICIONALES')
    self.genrerar_formulario()
    self.show()

  def genrerar_formulario(self):
    
    #Lables

    text_lbl = QLabel(self)
    text_lbl.setText('Ingrese un numero')
    text_lbl.setFont(QFont('Arial', 16))
    text_lbl.move(20,54)

    #Input

    self.intp =QLineEdit(self)
    self.intp.resize(250,24)
    self.intp.move(250,54)
    



if __name__ == '__main__':
  app = QApplication(sys.argv)
  form = Ventana()
  form.show()
  sys.exit(app.exec())