import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QVBoxLayout, QHBoxLayout, 
                             QCheckBox, QSlider, QProgressBar, QLineEdit, 
                             QComboBox, QLabel, QCalendarWidget)
from PyQt5.QtCore import Qt

class PanelWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # 1. Entrada de texto y Combo
        self.qle = QLineEdit(self)
        self.qle.setPlaceholderText("Escribe algo aquí...")
        
        self.combo = QComboBox(self)
        self.combo.addItems(["Opción A", "Opción B", "Opción C"])

        # 2. Slider y Progreso sincronizados
        self.pbar = QProgressBar(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(self.pbar.setValue) # El slider mueve la barra

        # 3. Checkbox y Calendario
        self.cb = QCheckBox('Activar Calendario', self)
        self.cal = QCalendarWidget(self)
        self.cal.setEnabled(False) # Empezamos desactivado
        self.cb.stateChanged.connect(lambda: self.cal.setEnabled(self.cb.isChecked()))

        # Añadir todo al layout
        layout.addWidget(QLabel("Entrada de Usuario:"))
        layout.addWidget(self.qle)
        layout.addWidget(self.combo)
        layout.addWidget(QLabel("Control de Progreso:"))
        layout.addWidget(sld)
        layout.addWidget(self.pbar)
        layout.addWidget(self.cb)
        layout.addWidget(self.cal)

        self.setLayout(layout)
        self.setWindowTitle('Catálogo de Widgets PyQt5')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PanelWidgets()
    sys.exit(app.exec_())