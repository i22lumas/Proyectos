import sys
from pathlib import Path
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QTextEdit, QInputDialog, QColorDialog, 
                             QFontDialog, QFileDialog, QLabel)
from PyQt5.QtGui import QColor

class SuiteDialogos(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Widget Central y Layout
        self.centro = QWidget()
        self.setCentralWidget(self.centro)
        layout = QVBoxLayout()

        # 2. Elementos de la Interfaz
        self.lbl_usuario = QLabel('Usuario: Invitado', self)
        self.editor = QTextEdit(self)
        self.editor.setPlaceholderText("El contenido del archivo aparecerá aquí...")

        # 3. Botones para disparar los Diálogos
        btn_nombre = QPushButton('1. Cambiar Nombre (QInputDialog)')
        btn_color = QPushButton('2. Color de Fondo (QColorDialog)')
        btn_fuente = QPushButton('3. Cambiar Fuente (QFontDialog)')
        btn_archivo = QPushButton('4. Abrir Archivo (QFileDialog)')

        # Conectar señales a los métodos de diálogo
        btn_nombre.clicked.connect(self.dialogoNombre)
        btn_color.clicked.connect(self.dialogoColor)
        btn_fuente.clicked.connect(self.dialogoFuente)
        btn_archivo.clicked.connect(self.dialogoArchivo)

        # Añadir widgets al layout
        layout.addWidget(self.lbl_usuario)
        layout.addWidget(btn_nombre)
        layout.addWidget(btn_color)
        layout.addWidget(btn_fuente)
        layout.addWidget(btn_archivo)
        layout.addWidget(self.editor)

        self.centro.setLayout(layout)
        self.setWindowTitle('Demostración de Diálogos PyQt5')
        self.setGeometry(300, 300, 500, 450)
        self.show()

    # --- MÉTODOS DE DIÁLOGO ---

    def dialogoNombre(self):
        # Captura un string simple
        texto, ok = QInputDialog.getText(self, 'Nombre', 'Introduce tu nombre:')
        if ok and texto:
            self.lbl_usuario.setText(f'Usuario: {texto}')

    def dialogoColor(self):
        # Selecciona un color y lo aplica mediante StyleSheet
        color = QColorDialog.getColor()
        if color.isValid():
            self.centro.setStyleSheet(f"background-color: {color.name()};")

    def dialogoFuente(self):
        # Selecciona una fuente y la aplica al editor de texto
        fuente, ok = QFontDialog.getFont()
        if ok:
            self.editor.setFont(fuente)

    def dialogoArchivo(self):
        # Selecciona un archivo del sistema y lee su contenido
        home = str(Path.home())
        ruta, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', home, "Textos (*.txt);;Todos (*)")
        
        if ruta:
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
                self.editor.setText(contenido)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SuiteDialogos()
    sys.exit(app.exec_())