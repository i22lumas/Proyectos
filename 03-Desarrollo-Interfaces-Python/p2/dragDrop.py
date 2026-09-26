import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class BotonArrastrable(QPushButton):
    def mouseMoveEvent(self, e):
        # Solo arrastramos con el botón derecho
        if e.buttons() == Qt.RightButton:
            drag = QDrag(self)
            mime_data = QMimeData() # Datos vacíos, solo queremos mover el objeto
            drag.setMimeData(mime_data)
            
            # Ajustamos el punto de agarre (HotSpot)
            drag.setHotSpot(e.pos() - self.rect().topLeft())
            drag.exec_(Qt.MoveAction)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True) # La ventana acepta que le "suelten" cosas
        self.btn = BotonArrastrable('Muéveme con clic derecho', self)
        self.btn.move(100, 100)
        self.btn.resize(200, 50)
        
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Práctica de Drag & Drop')
        self.show()

    def dragEnterEvent(self, e):
        e.accept() # Aceptamos cualquier entrada en la ventana

    def dropEvent(self, e):
        # Al soltar, movemos el botón a la posición del ratón
        self.btn.move(e.pos())
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VentanaPrincipal()
    sys.exit(app.exec_())