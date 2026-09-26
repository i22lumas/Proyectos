import os
from dataclasses import dataclass

@dataclass
class OpcionBuild:
    nombre: str
    viabilidad: str
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

class AdvisorModel:
    def __init__(self):
        # 1. Perfil del Cliente (Especificaciones y Presupuesto)
        self.presupuesto = 1000
        self.formato = "ATX (Estándar)"
        self.preferencia_marca = "Indiferente"
        
        # 2. Casos de Uso
        self.aplicaciones = []
        
        # Configuracion del Asesor (IA)
        self.modelo_llm = "Experto Hardware GPT-4"
        self.modo_web = False 
        
        # Resultados del Asesoramiento
        self.pdfs = []
        self.fuentes_web = []
        self.opciones_generadas = [] 
        self.recomendacion_principal = "" 
        self.justificacion_experto = ""

    def add_pdf(self, ruta):
        nombre = os.path.basename(ruta)
        tamano = f"{os.path.getsize(ruta) / 1024:.1f} KB"
        self.pdfs.append(PDFDocument(nombre, ruta, tamano))

    def clear_pdfs(self):
        self.pdfs.clear()