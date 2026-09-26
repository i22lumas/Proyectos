import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QToolTip, QMessageBox, QLabel, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class MiAplicacionPracticas(QWidget):

    def __init__(self):
        super().__init__()
        # Ejecutamos la configuración de la interfaz
        self.initUI()

    def initUI(self):
        # 1. Configuración de la Ventana
        self.setWindowTitle('Resumen PyQt5 - Informe de Prácticas')
        self.setWindowIcon(QIcon('logo.png')) # Icono de la ventana
        self.resize(400, 300)
        self.centrarVentana()

        # 2. Configuración de Estilos (Tooltips)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('Esta es la ventana principal de <b>QWidget</b>')

        # 3. Gestión de Fechas y Horas (Lógica interna)
        ahora = QDateTime.currentDateTime()
        fecha_str = ahora.toString(Qt.DefaultLocaleLongDate)
        unix_time = ahora.toSecsSinceEpoch()

        # 4. Creación de Widgets (Interfaz)
        layout = QVBoxLayout() # Organizador vertical

        self.lbl_info = QLabel(f"Hoy es: {fecha_str}\nUnix Time: {unix_time}", self)
        layout.addWidget(self.lbl_info)

        # Botón para mostrar un cálculo de fecha
        btn_fecha = QPushButton('Calcular días hasta Navidad', self)
        btn_fecha.setToolTip('Usa el método <b>daysTo</b> de QDate')
        btn_fecha.clicked.connect(self.mostrarDiasNavidad)
        layout.addWidget(btn_fecha)

        # Botón de Salida
        btn_salir = QPushButton('Cerrar Aplicación', self)
        btn_salir.clicked.connect(self.close) # Llama al evento de cierre
        layout.addWidget(btn_salir)

        self.setLayout(layout)
        self.show()

    def centrarVentana(self):
        """Calcula el centro de la pantalla y mueve la ventana allí"""
        geometria_ventana = self.frameGeometry()
        centro_pantalla = QApplication.desktop().availableGeometry().center()
        geometria_ventana.moveCenter(centro_pantalla)
        self.move(geometria_ventana.topLeft())

    def mostrarDiasNavidad(self):
        hoy = QDate.currentDate()
        navidad = QDate(hoy.year(), 12, 25)
        
        # Si ya pasó navidad este año, calculamos para el próximo
        if hoy > navidad:
            navidad = QDate(hoy.year() + 1, 12, 25)
            
        dias = hoy.daysTo(navidad)
        QMessageBox.information(self, 'Calendario', f'Faltan {dias} días para Navidad.')

    def closeEvent(self, event):
        """Sobreescritura del evento de cierre para confirmar salida"""
        respuesta = QMessageBox.question(self, 'Confirmar Salida',
                                       "¿Estás seguro de que deseas cerrar el programa?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if respuesta == QMessageBox.Yes:
            event.accept() # Cierra la app
        else:
            event.ignore() # Mantiene la app abierta

if __name__ == '__main__':
    # Todo programa PyQt5 empieza creando la aplicación
    app = QApplication(sys.argv)
    
    ejemplo = MiAplicacionPracticas()
    
    # El bucle principal de eventos
    sys.exit(app.exec_())