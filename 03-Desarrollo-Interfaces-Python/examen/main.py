import sys
from PyQt5.QtWidgets import QApplication

# Importamos la Arquitectura MVC
from modelo import AdvisorModel
from vista import MainWindow
from controlador import AdvisorController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # 1. Instanciar el Modelo (Cerebro de datos)
    modelo = AdvisorModel()
    
    # 2. Instanciar la Vista (Interfaz del usuario)
    vista = MainWindow()
    
    # 3. Conectar Modelo y Vista mediante el Controlador (Lógica experta)
    controlador = AdvisorController(modelo, vista)
    
    # Arrancar la aplicación
    vista.show()
    sys.exit(app.exec_())