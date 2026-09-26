import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, 
                             QPushButton, QLabel, QLCDNumber, QSlider)
from PyQt5.QtCore import Qt, pyqtSignal, QObject

# 1. SEÑAL PERSONALIZADA
# Creamos una clase para definir una señal que no existe en PyQt5
class Comunicador(QObject):
    alerta_maxima = pyqtSignal() # Definimos la señal

class AplicaciónInteractiva(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 2. SEÑALES Y SLOTS ESTÁNDAR
        # Conectamos un Slider con un número LCD
        self.lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        slider.setMaximum(100)
        
        # Conexión directa: la señal del slider alimenta al slot del LCD
        slider.valueChanged.connect(self.lcd.display)
        
        # 3. IDENTIFICACIÓN DEL EMISOR (sender)
        # Dos botones usan la misma función (slot)
        btn1 = QPushButton("Botón A")
        btn2 = QPushButton("Botón B")
        
        btn1.clicked.connect(self.identificar_boton)
        btn2.clicked.connect(self.identificar_boton)

        # Etiquetas de información
        self.lbl_info = QLabel("Presiona teclas o mueve el ratón", self)
        self.lbl_coords = QLabel("x: 0, y: 0", self)

        # 4. ACTIVAR RASTREO DE RATÓN (Mouse Tracking)
        self.setMouseTracking(True)

        # 5. INSTANCIAR SEÑAL PERSONALIZADA
        self.com = Comunicador()
        self.com.alerta_maxima.connect(self.accion_especial)

        # Añadir al layout
        layout.addWidget(self.lcd)
        layout.addWidget(slider)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(self.lbl_info)
        layout.addWidget(self.lbl_coords)

        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Eventos y Señales')
        self.show()

    # REIMPLEMENTACIÓN DE MANEJADORES DE EVENTOS
    def keyPressEvent(self, e):
        """Captura pulsaciones de teclado"""
        if e.key() == Qt.Key_Escape:
            self.close() # Cierra con Esc
        else:
            self.lbl_info.setText(f"Tecla presionada: {e.text()}")

    def mouseMoveEvent(self, e):
        """Captura movimiento del ratón mediante el objeto evento 'e'"""
        self.lbl_coords.setText(f"x: {e.x()}, y: {e.y()}")
        
        # Disparar señal personalizada si el ratón llega a x > 300
        if e.x() > 300:
            self.com.alerta_maxima.emit()

    def identificar_boton(self):
        """Uso de self.sender() para saber quién disparó la señal"""
        origen = self.sender()
        self.lbl_info.setText(f"Has pulsado el: {origen.text()}")

    def accion_especial(self):
        """Slot para la señal personalizada"""
        self.lbl_info.setText("¡ALERTA: Ratón en zona crítica!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplicaciónInteractiva()
    sys.exit(app.exec_())