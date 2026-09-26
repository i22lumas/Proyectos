from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QGridLayout, QCheckBox, QLabel, QSpinBox, 
                             QComboBox, QPushButton, QGroupBox, QRadioButton, 
                             QTableWidget, QTableWidgetItem, QDialog, 
                             QTextEdit, QHeaderView)

class PDFManagerDialog(QDialog):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.setWindowTitle("Conocimiento Local (Manuales y Specs)")
        self.resize(500, 300)
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Documento", "Ruta", "Peso"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Añadir PDF de Piezas")
        self.btn_clear = QPushButton("Vaciar Lista")
        self.btn_close = QPushButton("Cerrar")
        
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_clear)
        btn_layout.addWidget(self.btn_close)
        self.layout.addLayout(btn_layout)
        self.refresh_table()

    def refresh_table(self):
        self.table.setRowCount(len(self.model.pdfs))
        for row, pdf in enumerate(self.model.pdfs):
            self.table.setItem(row, 0, QTableWidgetItem(pdf.nombre))
            self.table.setItem(row, 1, QTableWidgetItem(pdf.ruta))
            self.table.setItem(row, 2, QTableWidgetItem(pdf.tamano))

class WebSourcesDialog(QDialog):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fuentes de Internet Consultadas")
        self.resize(500, 300)
        layout = QVBoxLayout(self)

        table = QTableWidget(len(model.fuentes_web), 3)
        table.setHorizontalHeaderLabels(["Web/Review", "URL", "Fecha Consulta"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row, web in enumerate(model.fuentes_web):
            table.setItem(row, 0, QTableWidgetItem(web.titulo))
            table.setItem(row, 1, QTableWidgetItem(web.url))
            table.setItem(row, 2, QTableWidgetItem(web.fecha))
        layout.addWidget(table)

class OpcionesDialog(QDialog):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Análisis de Opciones del Experto")
        self.resize(650, 250)
        layout = QVBoxLayout(self)

        table = QTableWidget(len(model.opciones_generadas), 3)
        table.setHorizontalHeaderLabels(["Build Propuesta", "Ajuste a Presupuesto", "Veredicto Técnico"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row, opt in enumerate(model.opciones_generadas):
            table.setItem(row, 0, QTableWidgetItem(opt.nombre))
            table.setItem(row, 1, QTableWidgetItem(opt.viabilidad))
            table.setItem(row, 2, QTableWidgetItem(opt.estado))
            
        layout.addWidget(table)

class TextDisplayDialog(QDialog):
    def __init__(self, titulo, contenido, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.resize(550, 400)
        layout = QVBoxLayout(self)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(contenido)
        # Dar formato de consola de experto
        text_edit.setStyleSheet("font-family: Consolas; font-size: 10pt; background-color: #f4f4f4;")
        layout.addWidget(text_edit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asesor Experto en Hardware - Configuración de PC (MVC)")
        self.resize(750, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 1. Panel de Presupuesto y Base
        specs_group = QGroupBox("1. Define tu Presupuesto y Preferencias Base")
        grid_specs = QGridLayout()
        
        grid_specs.addWidget(QLabel("Presupuesto Máximo (€):"), 0, 0)
        self.spin_presupuesto = QSpinBox()
        self.spin_presupuesto.setRange(300, 8000)
        self.spin_presupuesto.setSingleStep(50)
        self.spin_presupuesto.setValue(1200)
        grid_specs.addWidget(self.spin_presupuesto, 0, 1)

        grid_specs.addWidget(QLabel("Tamaño de la Torre:"), 0, 2)
        self.combo_formato = QComboBox()
        self.combo_formato.addItems(["ATX (Mid Tower Estándar)", "Micro-ATX (Torre Compacta)", "Mini-ITX (Cubo/SFF)"])
        grid_specs.addWidget(self.combo_formato, 0, 3)

        grid_specs.addWidget(QLabel("Preferencia CPU/GPU:"), 1, 0)
        self.combo_marca = QComboBox()
        self.combo_marca.addItems(["El mejor rendimiento/precio (Indiferente)", "Procesador AMD + Gráfica NVIDIA", "Todo AMD (Smart Access)", "Todo Intel/NVIDIA"])
        grid_specs.addWidget(self.combo_marca, 1, 1, 1, 3)

        specs_group.setLayout(grid_specs)
        main_layout.addWidget(specs_group)

        # 2. Panel de Casos de Uso
        apps_group = QGroupBox("2. ¿Para qué vas a usar principalmente el PC?")
        grid_apps = QGridLayout()
        
        self.chk_gaming = QCheckBox("Gaming AAA (Gráficos en Ultra, RayTracing)")
        self.chk_esports = QCheckBox("Gaming Competitivo (CS2, Valorant a 240Hz+)")
        self.chk_edicion = QCheckBox("Productividad (Premiere, Blender, AutoCAD)")
        self.chk_ofimatica = QCheckBox("Ofimática, Estudios y Multimedia")
        self.chk_ia = QCheckBox("Inteligencia Artificial (Entrenamiento Local / Stable Diffusion)")
        
        grid_apps.addWidget(self.chk_gaming, 0, 0)
        grid_apps.addWidget(self.chk_esports, 1, 0)
        grid_apps.addWidget(self.chk_edicion, 0, 1)
        grid_apps.addWidget(self.chk_ofimatica, 1, 1)
        grid_apps.addWidget(self.chk_ia, 2, 0, 1, 2)

        apps_group.setLayout(grid_apps)
        main_layout.addWidget(apps_group)

        # 3. Panel de Conocimiento del Asesor
        llm_group = QGroupBox("3. Base de Datos del Asesor")
        llm_layout = QVBoxLayout()
        
        self.rb_local = QRadioButton("Consultar solo Manuales/PDFs aportados (Offline)")
        self.rb_web = QRadioButton("Buscar benchmarks y precios actuales en Internet (Web + Local)")
        self.rb_web.setChecked(True)
        
        llm_layout.addWidget(self.rb_local)
        llm_layout.addWidget(self.rb_web)
        llm_group.setLayout(llm_layout)
        main_layout.addWidget(llm_group)

        # 4. Botonera del Experto
        btn_layout = QHBoxLayout()
        self.btn_opciones = QPushButton("Explorar Builds")
        self.btn_recomendacion = QPushButton("Ver Build Definitiva")
        self.btn_justificacion = QPushButton("Explicación Técnica del Asesor")
        self.btn_pdfs = QPushButton("Aportar Manuales (PDF)")
        self.btn_web = QPushButton("Fuentes Consultadas")
        
        # Estilos para resaltar los botones principales
        self.btn_recomendacion.setStyleSheet("background-color: #2b78e4; color: white; font-weight: bold;")
        self.btn_justificacion.setStyleSheet("background-color: #e67c00; color: white; font-weight: bold;")
        
        btn_layout.addWidget(self.btn_opciones)
        btn_layout.addWidget(self.btn_recomendacion)
        btn_layout.addWidget(self.btn_justificacion)
        btn_layout.addWidget(self.btn_pdfs)
        btn_layout.addWidget(self.btn_web)
        
        main_layout.addLayout(btn_layout)