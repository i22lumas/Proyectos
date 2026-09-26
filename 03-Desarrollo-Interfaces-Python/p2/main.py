import sys
from PyQt5.QtWidgets import QApplication
from modelo import ModeloEditor
from vista import VistaEditor
from controlador import ControladorEditor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Instanciamos los componentes del patrón MVC
    modelo = ModeloEditor()
    vista = VistaEditor()
    controlador = ControladorEditor(vista, modelo)
    
    # Vinculamos la vista con su controlador
    vista.set_controlador(controlador)
    
    # Arrancamos la interfaz
    vista.show()
    sys.exit(app.exec_())