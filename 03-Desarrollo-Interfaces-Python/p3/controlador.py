import os

class ControladorEditor:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def cargar_directorio(self, ruta):
        archivos = self.modelo.listar_archivos(ruta)
        self.vista.actualizar_lista(archivos)

    def abrir_archivo(self, directorio, nombre_archivo):
        ruta_completa = os.path.join(directorio, nombre_archivo)
        try:
            contenido = self.modelo.leer_archivo(ruta_completa)
            self.vista.mostrar_texto(contenido)
        except Exception as e:
            self.vista.mostrar_mensaje("Error", f"No se pudo leer: {e}", es_error=True)

    def guardar_archivo(self, directorio, nombre_archivo, contenido):
        ruta_completa = os.path.join(directorio, nombre_archivo)
        try:
            self.modelo.guardar_archivo(ruta_completa, contenido)
            self.vista.mostrar_mensaje("Éxito", "Archivo guardado correctamente.")
        except Exception as e:
            self.vista.mostrar_mensaje("Error", f"No se pudo guardar: {e}", es_error=True)

    def guardar_como(self, ruta_completa, contenido):
        try:
            self.modelo.guardar_archivo(ruta_completa, contenido)
            self.vista.mostrar_mensaje("Éxito", "Archivo guardado correctamente.")
            # Actualizamos la lista de archivos por si se guardó en la misma carpeta
            directorio = os.path.dirname(ruta_completa)
            if self.vista.txt_carpeta.text() == directorio:
                self.cargar_directorio(directorio)
        except Exception as e:
            self.vista.mostrar_mensaje("Error", f"No se pudo guardar: {e}", es_error=True)