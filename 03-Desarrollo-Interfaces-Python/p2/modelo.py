import os

class ModeloEditor:
    def listar_archivos(self, ruta_directorio):
        """Devuelve una lista con los archivos de un directorio."""
        archivos = []
        if os.path.exists(ruta_directorio) and os.path.isdir(ruta_directorio):
            archivos = [f for f in os.listdir(ruta_directorio) if os.path.isfile(os.path.join(ruta_directorio, f))]
        return archivos

    def leer_archivo(self, ruta_completa):
        """Lee y devuelve el contenido de un archivo."""
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            return f.read()

    def guardar_archivo(self, ruta_completa, contenido):
        """Guarda el texto en la ruta especificada."""
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        return True