import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, 
                             QLabel, QLineEdit, QTextEdit)

class EjemploLayouts(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # --- 1. LAYOUT DE CUADRÍCULA (QGridLayout) ---
        # Ideal para formularios donde queremos alinear etiquetas y campos
        grid = QGridLayout()
        grid.setSpacing(10) # Espacio entre los widgets

        # Añadimos widgets: addWidget(widget, fila, columna)
        grid.addWidget(QLabel('Título:'), 0, 0)
        grid.addWidget(QLineEdit(), 0, 1)

        grid.addWidget(QLabel('Autor:'), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel('Reseña:'), 2, 0)
        # addWidget(widget, fila, columna, rowSpan, columnSpan)
        # El QTextEdit ocupará 3 filas de alto y 1 columna de ancho
        grid.addWidget(QTextEdit(), 2, 1, 3, 1)

        # --- 2. LAYOUT HORIZONTAL (QHBoxLayout) ---
        # Lo usamos para la fila de botones en la parte inferior
        hbox = QHBoxLayout()
        
        # addStretch(1) crea un espacio elástico que empuja los botones a la derecha
        hbox.addStretch(1) 
        hbox.addWidget(QPushButton("Guardar"))
        hbox.addWidget(QPushButton("Cancelar"))

        # --- 3. LAYOUT VERTICAL PRINCIPAL (QVBoxLayout) ---
        # Este es el contenedor maestro que organiza los layouts anteriores
        vbox = QVBoxLayout()
        vbox.addLayout(grid) # Metemos la cuadrícula arriba
        vbox.addStretch(1)   # Metemos un espacio elástico intermedio
        vbox.addLayout(hbox) # Metemos los botones abajo

        # Establecemos el layout principal a la ventana
        self.setLayout(vbox)

        # Configuración visual de la ventana
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Layouts en PyQt5')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EjemploLayouts()
    sys.exit(app.exec_())