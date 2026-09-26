from PyQt5.QtWidgets import QFileDialog, QMessageBox
from modelo import OpcionBuild, FuenteWeb
from vista import OpcionesDialog, TextDisplayDialog, PDFManagerDialog, WebSourcesDialog

class AdvisorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_signals()

    def connect_signals(self):
        self.view.btn_opciones.clicked.connect(self.mostrar_opciones)
        self.view.btn_recomendacion.clicked.connect(self.mostrar_recomendacion)
        self.view.btn_justificacion.clicked.connect(self.mostrar_justificacion)
        self.view.btn_pdfs.clicked.connect(self.abrir_gestor_pdfs)
        self.view.btn_web.clicked.connect(self.abrir_fuentes_web)

    def actualizar_modelo_desde_vista(self):
        self.model.presupuesto = self.view.spin_presupuesto.value()
        self.model.formato = self.view.combo_formato.currentText()
        self.model.preferencia_marca = self.view.combo_marca.currentText()
        
        self.model.aplicaciones.clear()
        if self.view.chk_gaming.isChecked(): self.model.aplicaciones.append("Gaming AAA")
        if self.view.chk_esports.isChecked(): self.model.aplicaciones.append("Gaming Competitivo")
        if self.view.chk_edicion.isChecked(): self.model.aplicaciones.append("Productividad (Render/Edición)")
        if self.view.chk_ofimatica.isChecked(): self.model.aplicaciones.append("Ofimática")
        if self.view.chk_ia.isChecked(): self.model.aplicaciones.append("Inteligencia Artificial")
        
        self.model.modo_web = self.view.rb_web.isChecked()

    def simular_llm(self):
        self.model.opciones_generadas.clear()
        self.model.fuentes_web.clear()
        
        pto = self.model.presupuesto
        apps = self.model.aplicaciones
        
        # ==========================================
        # LÓGICA DEL ASESOR EXPERTO
        # ==========================================
        
        # Escenario 1: Productividad Pesada o IA
        if "Productividad (Render/Edición)" in apps or "Inteligencia Artificial" in apps:
            if pto >= 1800:
                self.model.opciones_generadas.append(OpcionBuild("Tier 1: i9-14900K + RTX 4080 Super + 64GB RAM", "Presupuesto Ideal", "Cero cuellos de botella. Rendimiento masivo en CUDA."))
                self.model.opciones_generadas.append(OpcionBuild("Tier 2: Ryzen 9 7950X + RTX 4070 Ti Super", "Ahorro de 200€", "Excelente multinúcleo, algo menos de VRAM."))
                
                self.model.recomendacion_principal = (
                    "Placa Base: Z790 ASUS ROG Tomahawk\n"
                    "CPU: Intel Core i9-14900K (24 Núcleos)\n"
                    "GPU: NVIDIA RTX 4080 Super 16GB VRAM\n"
                    "RAM: 64GB (2x32GB) DDR5 6400MHz CL30\n"
                    "Almacenamiento: 2TB Samsung 990 Pro NVMe PCIe 4.0\n"
                    "Fuente (PSU): Corsair 850W 80+ Gold ATX 3.0"
                )
                self.model.justificacion_experto = (
                    f"DIAGNÓSTICO DEL EXPERTO:\n"
                    f"Has seleccionado tareas críticas: {', '.join(apps)}. Para Inteligencia Artificial y Renderizado, "
                    f"la VRAM de la tarjeta gráfica y los núcleos CUDA de NVIDIA son innegociables. Por eso he descartado AMD Radeon.\n\n"
                    f"Con tu presupuesto de {pto}€, he configurado una bestia de productividad. Los 64GB de RAM DDR5 te permitirán cargar "
                    f"modelos pesados de IA y timelines de Premiere en 4K sin saturar el archivo de paginación. El SSD Gen4 asegura lecturas de 7000 MB/s."
                )
            else:
                self.model.opciones_generadas.append(OpcionBuild("Tier Entry: i5-13600K + RTX 4060 Ti 16GB", "Ajustado al máximo", "VRAM suficiente, CPU de gama media."))
                self.model.recomendacion_principal = "Intel i5-13600K, Placa B760, RTX 4060 Ti (Versión 16GB), 32GB RAM DDR5."
                self.model.justificacion_experto = (
                    f"DIAGNÓSTICO DEL EXPERTO:\n"
                    f"Tu presupuesto de {pto}€ es muy limitante para IA/Render profesional. He tenido que priorizar una tarjeta gráfica "
                    f"con 16GB de VRAM (RTX 4060 Ti) recortando en el procesador. Esto evitará que tus renders den error por falta de memoria, "
                    f"aunque los tiempos de exportación serán más lentos que en gamas altas."
                )

        # Escenario 2: Puramente Gaming AAA / eSports
        elif "Gaming AAA" in apps or "Gaming Competitivo" in apps:
            if pto >= 1300:
                self.model.opciones_generadas.append(OpcionBuild("Tier 1: Ryzen 7 7800X3D + RX 7900 GRE", "Perfecto", "El Rey del Gaming Actual."))
                self.model.opciones_generadas.append(OpcionBuild("Tier 2: Ryzen 5 7600X + RTX 4070 Super", "Buena opción RT", "Mejor RayTracing y DLSS 3."))
                
                self.model.recomendacion_principal = (
                    "Placa Base: B650 Gigabyte AORUS\n"
                    "CPU: AMD Ryzen 7 7800X3D\n"
                    "GPU: Sapphire AMD Radeon RX 7900 GRE 16GB\n"
                    "RAM: 32GB DDR5 6000MHz CL30 (Perfil EXPO)\n"
                    "Almacenamiento: 1TB WD Black SN850X\n"
                    "Fuente (PSU): MSI 750W 80+ Gold"
                )
                self.model.justificacion_experto = (
                    f"DIAGNÓSTICO DEL EXPERTO:\n"
                    f"Como quieres el PC para {', '.join(apps)}, la prioridad absoluta es sacar el máximo de FPS. "
                    f"El Ryzen 7 7800X3D es actualmente el mejor procesador de gaming del mundo gracias a su caché 3D masiva, "
                    f"lo que aniquila cualquier cuello de botella a 1080p y 1440p.\n\n"
                    f"Acompañado de la RX 7900 GRE, saturarás monitores de 240Hz en eSports y disfrutarás de texturas Ultra en AAA "
                    f"sin pasarte de tus {pto}€. He seleccionado memorias con perfil EXPO optimizado específicamente para AMD."
                )
            else:
                self.model.opciones_generadas.append(OpcionBuild("Tier 1080p: Ryzen 5 5600 + RX 7600", "Muy económico", "Rey de la gama de entrada. 1080p Ultra."))
                self.model.recomendacion_principal = "AMD Ryzen 5 5600, Placa B550M, Radeon RX 7600 8GB, 16GB RAM DDR4 3200MHz."
                self.model.justificacion_experto = (
                    f"DIAGNÓSTICO DEL EXPERTO:\n"
                    f"Con {pto}€ nos situamos en la gama de entrada. La decisión más técnica y rentable es quedarnos en la "
                    f"plataforma AM4 (DDR4). Ofrece el mejor ratio FPS/euro del mercado. Podrás jugar a todo en 1080p fluido."
                )

        # Escenario 3: Uso Básico
        else:
            self.model.opciones_generadas.append(OpcionBuild("Build Ofimática Larga Duración", "Sobrado", "PC silencioso y rápido para 10 años."))
            self.model.recomendacion_principal = "Intel Core i5-12400 (Gráficos UHD), 16GB RAM, SSD 1TB."
            self.model.justificacion_experto = (
                f"DIAGNÓSTICO DEL EXPERTO:\n"
                f"Para un uso ofimático, gastar {pto}€ en una tarjeta gráfica dedicada es tirar el dinero. "
                f"He configurado un sistema apoyado en un procesador potente con gráficos integrados, priorizando un disco "
                f"duro rápido y una fuente fiable. El sistema será virtualmente inaudible."
            )

        # Notas adicionales de factor de forma
        if self.model.formato == "Mini-ITX (Cubo/SFF)":
            self.model.justificacion_experto += (
                "\n\n⚠️ ADVERTENCIA DEL EXPERTO (MINI-ITX):\n"
                "Has elegido un formato SFF (Small Form Factor). Las temperaturas serán entre 5°C y 10°C más altas. "
                "Asegúrate de comprobar el 'Clearance' (espacio libre) del disipador de la CPU y elegir una fuente SFX."
            )

        self.model.justificacion_experto += f"\n\n[INFO] Manuales locales en contexto: {len(self.model.pdfs)}."

        if self.model.modo_web:
            self.model.fuentes_web.append(FuenteWeb("Tom's Hardware GPU Tier List 2026", "https://tomshardware.com/gpu-tiers", "2026-03-17"))
            self.model.fuentes_web.append(FuenteWeb("GamersNexus CPU Benchmarks", "https://gamersnexus.net/cpus", "2026-03-17"))
            self.model.justificacion_experto += "\n[INFO] Se han cruzado los datos de rendimiento con benchmarks web actualizados a hoy."

    def mostrar_opciones(self):
        self.actualizar_modelo_desde_vista()
        if not self.model.aplicaciones:
            QMessageBox.warning(self.view, "Datos Incompletos", "El asesor necesita saber para qué vas a usar el PC (Paso 2).")
            return
        self.simular_llm()
        dialog = OpcionesDialog(self.model, self.view)
        dialog.exec_()

    def mostrar_recomendacion(self):
        self.actualizar_modelo_desde_vista()
        if not self.model.aplicaciones:
            QMessageBox.warning(self.view, "Datos Incompletos", "El asesor necesita saber para qué vas a usar el PC (Paso 2).")
            return
        self.simular_llm()
        
        texto = f"=== BUILD DEFINITIVA DEL EXPERTO ===\n\n{self.model.recomendacion_principal}"
        dialog = TextDisplayDialog("Configuración Recomendada", texto, self.view)
        dialog.exec_()

    def mostrar_justificacion(self):
        self.actualizar_modelo_desde_vista()
        if not self.model.aplicaciones:
            QMessageBox.warning(self.view, "Datos Incompletos", "El asesor necesita saber para qué vas a usar el PC (Paso 2).")
            return
        self.simular_llm()
        dialog = TextDisplayDialog("Análisis Técnico", self.model.justificacion_experto, self.view)
        dialog.exec_()

    def abrir_gestor_pdfs(self):
        dialog = PDFManagerDialog(self.model, self.view)
        dialog.btn_add.clicked.connect(lambda: self.add_pdf_to_model(dialog))
        dialog.btn_clear.clicked.connect(lambda: self.clear_pdfs(dialog))
        dialog.btn_close.clicked.connect(dialog.close)
        dialog.exec_()

    def add_pdf_to_model(self, dialog):
        rutas, _ = QFileDialog.getOpenFileNames(self.view, "Aportar manuales de componentes", "", "Archivos PDF (*.pdf)")
        for ruta in rutas:
            self.model.add_pdf(ruta)
        dialog.refresh_table()

    def clear_pdfs(self, dialog):
        self.model.clear_pdfs()
        dialog.refresh_table()

    def abrir_fuentes_web(self):
        self.actualizar_modelo_desde_vista()
        if not self.model.modo_web:
            QMessageBox.warning(self.view, "Asesor Offline", "Le has indicado al asesor que no use Internet (Solo Local).")
            return
        self.simular_llm()
        dialog = WebSourcesDialog(self.model, self.view)
        dialog.exec_()