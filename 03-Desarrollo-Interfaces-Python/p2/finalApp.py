import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, 
                             QLineEdit, QComboBox, QAction, QMessageBox, 
                             QStatusBar, QToolBar, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class AplicacionPracticas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. CONFIGURACIÓN DEL WIDGET CENTRAL Y LAYOUTS
        # Usamos un widget central porque QMainWindow lo requiere para organizar layouts
        self.contenedor = QWidget()
        self.setCentralWidget(self.contenedor)
        
        layout_maestro = QVBoxLayout()
        
        # 2. DISEÑO DE FORMULARIO (QGridLayout)
        # Demuestra el posicionamiento alineado de controles
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(QLabel('Nombre del Usuario:'), 0, 0)
        self.input_nombre = QLineEdit()
        grid.addWidget(self.input_nombre, 0, 1)

        grid.addWidget(QLabel('Módulo de Práctica:'), 1, 0)
        self.combo_modulo = QComboBox()
        self.combo_modulo.addItems(['Interfaz Gráfica', 'Eventos', 'Bases de Datos', 'Pintura'])
        grid.addWidget(self.combo_modulo, 1, 1)

        grid.addWidget(QLabel('Opciones:'), 2, 0)
        self.check_log = QCheckBox('Habilitar registro de actividad')
        grid.addWidget(self.check_log, 2, 1)

        # 3. BARRA DE HERRAMIENTAS Y ACCIONES (QAction)
        # Creamos una acción reusable para el menú y la toolbar
        accion_limpiar = QAction(QIcon('clear.png'), 'Limpiar Formulario', self)
        accion_limpiar.setStatusTip('Borra todos los campos actuales')
        accion_limpiar.triggered.connect(self.limpiar_campos)

        accion_salir = QAction('Salir', self)
        accion_salir.triggered.connect(self.close)

        # Barra de Herramientas
        toolbar = self.addToolBar('Herramientas')
        toolbar.addAction(accion_limpiar)

        # 4. BARRA DE MENÚS
        menubar = self.menuBar()
        menu_archivo = menubar.addMenu('&Archivo')
        menu_archivo.addAction(accion_limpiar)
        menu_archivo.addSeparator()
        menu_archivo.addAction(accion_salir)

        # 5. BOTONES DE ACCIÓN (QHBoxLayout)
        # Demuestra el uso de espacios elásticos (Stretch)
        layout_botones = QHBoxLayout()
        btn_procesar = QPushButton('Procesar Datos')
        btn_procesar.clicked.connect(self.mostrar_resumen)
        
        layout_botones.addStretch(1) # Empuja el botón a la derecha
        layout_botones.addWidget(btn_procesar)

        # Ensamblar todo el layout principal
        layout_maestro.addLayout(grid)
        layout_maestro.addStretch(1) # Espacio entre formulario y botones
        layout_maestro.addLayout(layout_botones)
        self.contenedor.setLayout(layout_maestro)

        # 6. BARRA DE ESTADO (StatusBar)
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage('Aplicación iniciada correctamente')

        # Configuración final de la ventana
        self.setWindowTitle('Gestor de Prácticas PyQt5')
        self.setGeometry(300, 300, 450, 300)
        self.show()

    def limpiar_campos(self):
        """Limpia los widgets de control"""
        self.input_nombre.clear()
        self.combo_modulo.setCurrentIndex(0)
        self.check_log.setChecked(False)
        self.statusBar().showMessage('Formulario reiniciado')

    def mostrar_resumen(self):
        """Muestra un diálogo con los datos capturados"""
        nombre = self.input_nombre.text()
        modulo = self.combo_modulo.currentText()
        if not nombre:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese un nombre.')
            return
            
        resumen = f"Usuario: {nombre}\nModulo: {modulo}\nRegistro activo: {self.check_log.isChecked()}"
        QMessageBox.information(self, 'Resumen de Datos', resumen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplicacionPracticas()
    sys.exit(app.exec_())