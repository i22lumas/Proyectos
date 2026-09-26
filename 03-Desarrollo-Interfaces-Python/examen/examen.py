import sys
import os
from dataclasses import dataclass
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QGridLayout, QCheckBox, QLabel, 
                             QSpinBox, QComboBox, QPushButton, QGroupBox, 
                             QRadioButton, QTableWidget, QTableWidgetItem, 
                             QDialog, QTextEdit, QFileDialog, QHeaderView, QMessageBox)
from PyQt5.QtCore import Qt

# ==========================================
# 1. MODELO (M) - Mantiene el estado y datos
# ==========================================

@dataclass
class Hipotesis:
    nombre: str
    probabilidad: str
    estado: str

@dataclass
class PDFDocument:
    nombre: str
    ruta: str
    tamano: str

@dataclass
class FuenteWeb:
    titulo: str
    url: str
    fecha: str

class DiagnosticModel:
    def __init__(self):
        # Entradas del usuario
        self.sintomas = []
        self.temperatura = 0
        self.voltaje = 0.0
        self.nivel_ruido = "Normal"
        
        # Configuracion LLM
        self.modelo_llm = "gpt-4-turbo"
        self.modo_web = False # False = Solo local, True = Web + Local
        
        # Datos del sistema
        self.pdfs = []
        self.fuentes_web = []
        self.hipotesis_generadas = []
        self.diagnostico_final = ""
        self.justificacion = ""

    def add_pdf(self, ruta):
        nombre = os.path.basename(ruta)
        tamano = f"{os.path.getsize(ruta) / 1024:.1f} KB"
        self.pdfs.append(PDFDocument(nombre, ruta, tamano))

    def clear_pdfs(self):
        self.pdfs.clear()

# ==========================================
# 2. VISTAS (V) - Componentes Gráficos (UI)
# ==========================================

class PDFManagerDialog(QDialog):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model
        self.setWindowTitle("Gestión de PDFs")
        self.resize(500, 300)
        self.layout = QVBoxLayout(self)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Nombre", "Ruta", "Tamaño"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Añadir PDF")
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
        self.setWindowTitle("Fuentes Web Utilizadas")
        self.resize(500, 300)
        layout = QVBoxLayout(self)

        table = QTableWidget(len(model.fuentes_web), 3)
        table.setHorizontalHeaderLabels(["Título", "URL", "Fecha Acceso"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row, web in enumerate(model.fuentes_web):
            table.setItem(row, 0, QTableWidgetItem(web.titulo))
            table.setItem(row, 1, QTableWidgetItem(web.url))
            table.setItem(row, 2, QTableWidgetItem(web.fecha))
            
        layout.addWidget(table)

class HipotesisDialog(QDialog):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hipótesis Posibles")
        self.resize(500, 250)
        layout = QVBoxLayout(self)

        table = QTableWidget(len(model.hipotesis_generadas), 3)
        table.setHorizontalHeaderLabels(["Hipótesis", "Probabilidad", "Estado"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        for row, hip in enumerate(model.hipotesis_generadas):
            table.setItem(row, 0, QTableWidgetItem(hip.nombre))
            table.setItem(row, 1, QTableWidgetItem(hip.probabilidad))
            table.setItem(row, 2, QTableWidgetItem(hip.estado))
            
        layout.addWidget(table)

class TextDisplayDialog(QDialog):
    def __init__(self, titulo, contenido, parent=None):
        super().__init__(parent)
        self.setWindowTitle(titulo)
        self.resize(450, 300)
        layout = QVBoxLayout(self)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(contenido)
        layout.addWidget(text_edit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Diagnóstico ISSBC - PC Hardware")
        self.resize(600, 450)

        # Widget Central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- Panel de Síntomas ---
        sintomas_group = QGroupBox("Entrada de Síntomas y Observables")
        grid = QGridLayout()
        
        self.chk_enciende = QCheckBox("No enciende")
        self.chk_ruido = QCheckBox("Ruido extraño")
        self.chk_conexion = QCheckBox("Conexión perdida")
        self.chk_calor = QCheckBox("Sobrecalentamiento")
        
        grid.addWidget(self.chk_enciende, 0, 0)
        grid.addWidget(self.chk_ruido, 1, 0)
        grid.addWidget(self.chk_conexion, 2, 0)
        grid.addWidget(self.chk_calor, 3, 0)

        grid.addWidget(QLabel("Temperatura (°C):"), 0, 1)
        self.spin_temp = QSpinBox()
        self.spin_temp.setRange(20, 120)
        self.spin_temp.setValue(40)
        grid.addWidget(self.spin_temp, 0, 2)

        grid.addWidget(QLabel("Nivel de Ruido:"), 1, 1)
        self.combo_ruido = QComboBox()
        self.combo_ruido.addItems(["Bajo", "Normal", "Alto"])
        grid.addWidget(self.combo_ruido, 1, 2)

        sintomas_group.setLayout(grid)
        main_layout.addWidget(sintomas_group)

        # --- Panel de Configuración LLM ---
        llm_group = QGroupBox("Configuración del Modelo LLM")
        llm_layout = QVBoxLayout()
        
        combo_layout = QHBoxLayout()
        combo_layout.addWidget(QLabel("Modelo LLM:"))
        self.combo_llm = QComboBox()
        self.combo_llm.addItems(["gpt-4-turbo", "gpt-3.5", "llama-3"])
        combo_layout.addWidget(self.combo_llm)
        llm_layout.addLayout(combo_layout)

        self.rb_local = QRadioButton("Sólo PDFs locales")
        self.rb_web = QRadioButton("Toda la información fiable (PDFs y web)")
        self.rb_local.setChecked(True)
        
        llm_layout.addWidget(QLabel("Usar:"))
        llm_layout.addWidget(self.rb_local)
        llm_layout.addWidget(self.rb_web)
        
        llm_group.setLayout(llm_layout)
        main_layout.addWidget(llm_group)

        # --- Botonera Inferior ---
        btn_layout = QHBoxLayout()
        self.btn_hipotesis = QPushButton("Evaluar Hipótesis")
        self.btn_diagnostico = QPushButton("Diagnosticar")
        self.btn_justificacion = QPushButton("Justificación")
        self.btn_pdfs = QPushButton("Gestión (PDFs)")
        self.btn_web = QPushButton("Fuentes Web")
        
        btn_layout.addWidget(self.btn_hipotesis)
        btn_layout.addWidget(self.btn_diagnostico)
        btn_layout.addWidget(self.btn_justificacion)
        btn_layout.addWidget(self.btn_pdfs)
        btn_layout.addWidget(self.btn_web)
        
        main_layout.addLayout(btn_layout)

# ==========================================
# 3. CONTROLADOR (C) - Lógica y Coordinación
# ==========================================

class DiagnosticController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        # Conectar botones principales
        self.view.btn_hipotesis.clicked.connect(self.evaluar_hipotesis)
        self.view.btn_diagnostico.clicked.connect(self.mostrar_diagnostico)
        self.view.btn_justificacion.clicked.connect(self.mostrar_justificacion)
        self.view.btn_pdfs.clicked.connect(self.abrir_gestor_pdfs)
        self.view.btn_web.clicked.connect(self.abrir_fuentes_web)

    def actualizar_modelo_desde_vista(self):
        """Actualiza el modelo con los datos actuales de la interfaz"""
        self.model.sintomas.clear()
        if self.view.chk_enciende.isChecked(): self.model.sintomas.append("No enciende")
        if self.view.chk_ruido.isChecked(): self.model.sintomas.append("Ruido extraño")
        if self.view.chk_conexion.isChecked(): self.model.sintomas.append("Conexión perdida")
        if self.view.chk_calor.isChecked(): self.model.sintomas.append("Sobrecalentamiento")
        
        self.model.temperatura = self.view.spin_temp.value()
        self.model.nivel_ruido = self.view.combo_ruido.currentText()
        self.model.modelo_llm = self.view.combo_llm.currentText()
        self.model.modo_web = self.view.rb_web.isChecked()

    def simular_llm(self):
        """Simula la respuesta de la IA basándose en el estado del modelo"""
        self.model.hipotesis_generadas.clear()
        self.model.fuentes_web.clear()
        
        if "No enciende" in self.model.sintomas:
            self.model.hipotesis_generadas.append(Hipotesis("Fuente de alimentación defectuosa", "85%", "Posible"))
            self.model.diagnostico_final = "Fallo crítico en la fuente de alimentación."
            
        elif "Sobrecalentamiento" in self.model.sintomas or self.model.temperatura > 80:
            self.model.hipotesis_generadas.append(Hipotesis("Problema de refrigeración térmica", "90%", "Muy Probable"))
            self.model.diagnostico_final = "Sistema de ventilación obstruido o pasta térmica seca."
            
        elif "Ruido extraño" in self.model.sintomas:
            self.model.hipotesis_generadas.append(Hipotesis("Disco Duro HDD dañado", "60%", "Posible"))
            self.model.hipotesis_generadas.append(Hipotesis("Ventilador rozando cable", "40%", "Posible"))
            self.model.diagnostico_final = "Desgaste mecánico en HDD o ventilador."
        else:
            self.model.hipotesis_generadas.append(Hipotesis("Sin datos suficientes", "-", "Descartada"))
            self.model.diagnostico_final = "Introduce más síntomas para diagnosticar."

        # Simular justificación
        self.model.justificacion = (
            f"Basado en los síntomas: {', '.join(self.model.sintomas)}\n"
            f"Temperatura registrada: {self.model.temperatura}°C\n\n"
            f"El modelo {self.model.modelo_llm} ha determinado que el diagnóstico más "
            f"probable es: {self.model.diagnostico_final}\n\n"
            f"Evidencias usadas de PDFs locales: {len(self.model.pdfs)} ficheros."
        )

        # Añadir fuentes web fakes si el modo web está activo
        if self.model.modo_web:
            self.model.fuentes_web.append(FuenteWeb("Solución PC no enciende", "https://hardware-forum.com/fix", "2026-03-17"))
            self.model.justificacion += "\nSe consultaron fuentes web para validar la temperatura crítica."

    def evaluar_hipotesis(self):
        self.actualizar_modelo_desde_vista()
        self.simular_llm()
        dialog = HipotesisDialog(self.model, self.view)
        dialog.exec_()

    def mostrar_diagnostico(self):
        self.actualizar_modelo_desde_vista()
        self.simular_llm()
        dialog = TextDisplayDialog("Diagnóstico Final", self.model.diagnostico_final, self.view)
        dialog.exec_()

    def mostrar_justificacion(self):
        self.actualizar_modelo_desde_vista()
        self.simular_llm()
        dialog = TextDisplayDialog("Justificación del LLM", self.model.justificacion, self.view)
        dialog.exec_()

    def abrir_gestor_pdfs(self):
        dialog = PDFManagerDialog(self.model, self.view)
        dialog.btn_add.clicked.connect(lambda: self.add_pdf_to_model(dialog))
        dialog.btn_clear.clicked.connect(lambda: self.clear_pdfs(dialog))
        dialog.btn_close.clicked.connect(dialog.close)
        dialog.exec_()

    def add_pdf_to_model(self, dialog):
        rutas, _ = QFileDialog.getOpenFileNames(self.view, "Seleccionar PDF", "", "Archivos PDF (*.pdf)")
        for ruta in rutas:
            self.model.add_pdf(ruta)
        dialog.refresh_table()

    def clear_pdfs(self, dialog):
        self.model.clear_pdfs()
        dialog.refresh_table()

    def abrir_fuentes_web(self):
        self.actualizar_modelo_desde_vista()
        if not self.model.modo_web:
            QMessageBox.warning(self.view, "Modo Local Activo", "El modo web está desactivado. No se usó internet.")
            return
        self.simular_llm()
        dialog = WebSourcesDialog(self.model, self.view)
        dialog.exec_()


# ==========================================
# ARRANQUE DE LA APLICACIÓN
# ==========================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 1. Instanciar el Modelo
    modelo = DiagnosticModel()
    
    # 2. Instanciar la Vista
    vista = MainWindow()
    
    # 3. Conectar mediante el Controlador
    controlador = DiagnosticController(modelo, vista)
    
    vista.show()
    sys.exit(app.exec_())