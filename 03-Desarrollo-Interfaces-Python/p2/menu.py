import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QAction, 
                             QTextEdit, QMessageBox, QMenu, qApp)
from PyQt5.QtGui import QIcon

class VentanaProfesional(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 1. Widget Central: Un editor de texto que ocupa el espacio principal
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # 2. Creación de una Acción (QAction) reusable
        # Nota: He usado nombres de iconos estándar, asegúrate de tener los archivos .png
        exitAct = QAction(QIcon('exit.png'), '&Salir', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Cerrar la aplicación definitivamente')
        exitAct.triggered.connect(self.close)

        # 3. Barra de Estado
        self.statusBar().showMessage('Listo')

        # 4. Barra de Menús
        menubar = self.menuBar()
        # Para macOS: menubar.setNativeMenuBar(False) 
        
        fileMenu = menubar.addMenu('&Archivo')
        
        # Submenú dentro de Archivo
        importMenu = QMenu('Importar', self)
        importAct = QAction('Importar Datos...', self)
        importMenu.addAction(importAct)
        
        fileMenu.addMenu(importMenu) # Añadimos el submenú
        fileMenu.addSeparator()      # Línea divisoria
        fileMenu.addAction(exitAct)   # Añadimos la acción de salir

        # Menú de Ver (Checkable)
        viewMenu = menubar.addMenu('&Ver')
        viewStatAct = QAction('Ver barra de estado', self, checkable=True)
        viewStatAct.setStatusTip('Muestra u oculta la barra inferior')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleStatusBar)
        viewMenu.addAction(viewStatAct)

        # 5. Barra de Herramientas (Toolbar)
        toolbar = self.addToolBar('Salida')
        toolbar.addAction(exitAct)

        # 6. Configuración de la ventana principal
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Ejemplo Tutorial Menu')
        self.show()

    def toggleStatusBar(self, state):
        """Muestra u oculta la barra de estado según el menú 'Ver'"""
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()

    def contextMenuEvent(self, event):
        """Crea un menú emergente al hacer clic derecho"""
        cmenu = QMenu(self)
        
        newAct = cmenu.addAction("Nuevo")
        openAct = cmenu.addAction("Abrir")
        quitAct = cmenu.addAction("Salir")
        
        # Ejecuta el menú en la posición del ratón
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            qApp.quit()

    def closeEvent(self, event):
        """Confirmación antes de salir"""
        reply = QMessageBox.question(self, 'Salir', 
            "¿Deseas cerrar la aplicación?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VentanaProfesional()
    sys.exit(app.exec_())