from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
                             QGridLayout, QTextEdit, QListWidget, QFileDialog, QMessageBox)

class VistaEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.controlador = None
        self.initUI()

    def set_controlador(self, controlador):
        self.controlador = controlador

    def initUI(self):
        self.setWindowTitle("Editor de Archivos MVC")
        self.setMinimumSize(700, 500)

        # 1. Creación de Widgets
        self.lbl_carpeta = QLabel("Carpeta:")
        self.txt_carpeta = QLineEdit()
        self.txt_carpeta.setReadOnly(True) # Evita escribir a mano la ruta
        self.btn_seleccionar = QPushButton("Seleccionar")
        
        self.lbl_archivos = QLabel("Archivos")
        self.lista_archivos = QListWidget()
        self.editor = QTextEdit()
        
        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar_como = QPushButton("Salvar como")

        # 2. Organización en Cuadrícula (QGridLayout)
        grid = QGridLayout(self)
        grid.addWidget(self.lbl_carpeta, 0, 0)
        grid.addWidget(self.txt_carpeta, 0, 1)
        grid.addWidget(self.btn_seleccionar, 0, 2)
        
        grid.addWidget(self.lbl_archivos, 1, 0)
        
        grid.addWidget(self.lista_archivos, 2, 0, 1, 1) # Ocupa 1 fila, 1 columna
        grid.addWidget(self.editor, 2, 1, 1, 2)         # Ocupa 1 fila, 2 columnas
        
        grid.addWidget(self.btn_salvar, 3, 0)
        grid.addWidget(self.btn_salvar_como, 3, 1)

        # 3. Conexión de señales a funciones internas de la vista
        self.btn_seleccionar.clicked.connect(self.click_seleccionar)
        self.lista_archivos.itemDoubleClicked.connect(self.doble_click_lista)
        self.btn_salvar.clicked.connect(self.click_salvar)
        self.btn_salvar_como.clicked.connect(self.click_salvar_como)

    # --- Delegación al Controlador ---
    def click_seleccionar(self):
        carpeta = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        if carpeta and self.controlador:
            self.txt_carpeta.setText(carpeta)
            self.controlador.cargar_directorio(carpeta)

    def doble_click_lista(self, item):
        if self.controlador:
            nombre_archivo = item.text()
            directorio = self.txt_carpeta.text()
            self.controlador.abrir_archivo(directorio, nombre_archivo)

    def click_salvar(self):
        item_actual = self.lista_archivos.currentItem()
        if item_actual and self.controlador:
            nombre_archivo = item_actual.text()
            directorio = self.txt_carpeta.text()
            contenido = self.editor.toPlainText()
            self.controlador.guardar_archivo(directorio, nombre_archivo, contenido)
        else:
            self.click_salvar_como()

    def click_salvar_como(self):
        ruta, _ = QFileDialog.getSaveFileName(self, 'Salvar como', self.txt_carpeta.text(), "Todos (*);;Textos (*.txt)")
        if ruta and self.controlador:
            contenido = self.editor.toPlainText()
            self.controlador.guardar_como(ruta, contenido)

    # --- Actualizaciones visuales ordenadas por el Controlador ---
    def actualizar_lista(self, archivos):
        self.lista_archivos.clear()
        self.lista_archivos.addItems(archivos)
        self.editor.clear()

    def mostrar_texto(self, texto):
        self.editor.setText(texto)

    def mostrar_mensaje(self, titulo, mensaje, es_error=False):
        if es_error:
            QMessageBox.critical(self, titulo, mensaje)
        else:
            QMessageBox.information(self, titulo, mensaje)