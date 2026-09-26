import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt

class LienzoArte(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Práctica de Pintura en PyQt5')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def paintEvent(self, event):
        # El pintor siempre se inicializa en el evento de pintura
        qp = QPainter()
        qp.begin(self)
        
        # 1. Dibujar Texto con Estilo
        qp.setPen(QColor(50, 50, 200)) # Azul
        qp.setFont(QFont('Verdana', 12, QFont.Bold))
        qp.drawText(event.rect(), Qt.AlignTop | Qt.AlignHCenter, "Gráficos Vectoriales")

        # 2. Dibujar con Pluma (QPen) Personalizada
        pen = QPen(Qt.red, 3, Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20, 60, 380, 60) # Línea discontinua roja

        # 3. Dibujar Rectángulos con Pinceles (QBrush)
        # Rectángulo sólido con transparencia (Alpha = 150)
        qp.setBrush(QColor(0, 255, 0, 150)) 
        qp.setPen(Qt.black)
        qp.drawRect(50, 100, 100, 100)

        # Rectángulo con patrón de sombreado
        brush = QBrush(Qt.Dense4Pattern)
        qp.setBrush(brush)
        qp.drawRect(230, 100, 100, 100)

        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LienzoArte()
    sys.exit(app.exec_())