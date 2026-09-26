import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTextEdit, QAction, 
                             QFileDialog, QMessageBox, QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon

class EditorTextos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.archivo_actual = None
        self.initUI()

    def initUI(self):
        # 1. Widget Central
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        
        # 2. Acciones de Archivo
        # Abrir
        openAct = QAction(QIcon('open.png'), '&Abrir', self)
        openAct.setShortcut('Ctrl+O')
        openAct.triggered.connect(self.abrir_archivo)

        # Guardar
        saveAct = QAction(QIcon('save.png'), '&Guardar', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.triggered.connect(self.guardar_archivo)

        # Guardar Como
        saveAsAct = QAction('&Guardar como...', self)
        saveAsAct.triggered.connect(self.guardar_como)

        # Salir
        exitAct = QAction('&Salir', self)
        exitAct.triggered.connect(self.close)

        # 3. Barra de Menús
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)

        # 4. Configuración Ventana
        self.statusBar().showMessage('Listo')
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('PyNote - Nuevo Archivo')
        self.show()

    # --- LÓGICA DE ARCHIVOS ---

    def abrir_archivo(self):
        ruta, _ = QFileDialog.getOpenFileName(self, 'Abrir archivo', '', "Textos (*.txt);;Todos (*)")
        if ruta:
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    self.editor.setText(f.read())
                self.archivo_actual = ruta
                self.actualizar_titulo()
                self.statusBar().showMessage(f'Abierto: {ruta}')
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir: {e}")

    def guardar_archivo(self):
        if self.archivo_actual:
            try:
                with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                self.statusBar().showMessage('Guardado con éxito')
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar: {e}")
        else:
            self.guardar_como()

    def guardar_como(self):
        ruta, _ = QFileDialog.getSaveFileName(self, 'Guardar como', '', "Textos (*.txt);;Todos (*)")
        if ruta:
            self.archivo_actual = ruta
            self.guardar_archivo()
            self.actualizar_titulo()

    def actualizar_titulo(self):
        self.setWindowTitle(f'PyNote - {self.archivo_actual}')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmar', "¿Deseas cerrar el editor?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditorTextos()
    sys.exit(app.exec_())