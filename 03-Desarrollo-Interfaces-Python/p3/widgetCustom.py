import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, 
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QPainter, QFont, QColor, QPen

# 1. CLASE DE COMUNICACIÓN
# Se usa para definir señales personalizadas que conecten widgets
class Comunicador(QObject):
    actualizar_valor = pyqtSignal(int)

# 2. EL WIDGET PERSONALIZADO (Custom Widget)
# Hereda de QWidget para tener un lienzo en blanco
class WidgetCapacidad(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(1, 30)
        self.valor = 75 # Valor inicial
        self.escala = [75, 150, 225, 300, 375, 450, 525, 600, 675]

    def recibir_valor(self, nuevo_valor):
        self.valor = nuevo_valor

    def paintEvent(self, e):
        # El método paintEvent es donde ocurre la magia del dibujo
        qp = QPainter()
        qp.begin(self)
        self.dibujar_componente(qp)
        qp.end()

    def dibujar_componente(self, qp):
        MAX_NORMAL = 700
        MAX_TOTAL = 750

        # Configuración de fuente y medidas
        qp.setFont(QFont('Serif', 7, QFont.Light))
        ancho_v = self.size().width()
        alto_v = self.size().height()

        # Cálculo proporcional del llenado
        punto_llenado = int(((ancho_v / MAX_TOTAL) * self.valor))
        punto_critico = int(((ancho_v / MAX_TOTAL) * MAX_NORMAL))

        # Lógica de colores: Amarillo para normal, Rojo para exceso
        if self.valor >= MAX_NORMAL:
            # Dibuja parte amarilla hasta el límite
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, punto_critico, alto_v)
            # Dibuja parte roja el excedente
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(punto_critico, 0, punto_llenado - punto_critico, alto_v)
        else:
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, punto_llenado, alto_v)

        # Dibujar el contorno del widget
        qp.setPen(QColor(20, 20, 20))
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, ancho_v - 1, alto_v - 1)

        # Dibujar la escala numérica
        paso = int(round(ancho_v / 10))
        for i in range(1, 10):
            x_linea = i * paso
            qp.drawLine(x_linea, 0, x_linea, 5)
            
            # Centrar el texto de la escala usando métricas de fuente
            ancho_texto = qp.fontMetrics().width(str(self.escala[i-1]))
            qp.drawText(int(x_linea - ancho_texto/2), int(alto_v / 2), str(self.escala[i-1]))

# 3. VENTANA PRINCIPAL (Contenedor)
class EjemploCustomWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Slider para controlar el widget personalizado
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setRange(1, 750)
        self.sld.setValue(75)

        # Instanciar el widget personalizado y la señal
        self.comun = Comunicador()
        self.mi_widget = WidgetCapacidad()

        # Conexiones: Slider -> Señal -> Widget Personalizado
        self.comun.actualizar_valor.connect(self.mi_widget.recibir_valor)
        self.sld.valueChanged.connect(self.notificar_cambio)

        # Diseño: El widget personalizado se coloca abajo
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.mi_widget)
        vbox.addWidget(self.sld)
        
        self.setLayout(vbox)
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Widget Personalizado: Medidor de Capacidad')
        self.show()

    def notificar_cambio(self, v):
        self.comun.actualizar_valor.emit(v)
        self.mi_widget.repaint() # Forzar el redibujado inmediato

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EjemploCustomWidget()
    sys.exit(app.exec_())