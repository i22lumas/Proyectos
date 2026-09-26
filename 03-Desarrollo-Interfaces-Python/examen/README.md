1. Dominio elegido y breve descripción
Dominio: Asesoramiento, configuración y compatibilidad de hardware de PC.
Descripción: Esta aplicación actúa como la interfaz de un sistema experto (LLM) especializado en hardware informático. En lugar de diagnosticar averías tradicionales, el sistema evalúa los "síntomas" del usuario (presupuesto disponible, tamaño del chasis, preferencia de marcas y casos de uso como Gaming, IA o Edición de vídeo) para diagnosticar posibles cuellos de botella y recomendar la mejor configuración de componentes (PC Build) posible. El sistema justifica técnicamente sus decisiones basándose en manuales aportados por el usuario (PDFs locales) y, de forma opcional, en información de benchmarks de Internet.

2. Instrucciones de ejecución
Para ejecutar la aplicación correctamente en tu entorno local (Spyder o terminal), sigue estos pasos:
Requisitos previos: Asegúrate de tener instalado Python 3.x y la librería PyQt5 en tu entorno. Puedes instalarla ejecutando: pip install PyQt5
Estructura de archivos: Debes tener los cuatro archivos proporcionados guardados en la misma carpeta:
modelo.py
vista.py
controlador.py
main.py
Ejecución: * Desde Spyder: Abre únicamente el archivo main.py y presiona el botón de Play (o F5).
Desde Terminal: Navega hasta el directorio donde guardaste los archivos y ejecuta: python main.py

3. Descripción de la arquitectura MVC usada
El proyecto se ha dividido en cuatro archivos físicos para garantizar una separación estricta de responsabilidades, cumpliendo rigurosamente con el patrón Modelo-Vista-Controlador:
Modelo (modelo.py): Contiene la clase AdvisorModel y estructuras de datos puras (@dataclass). Su única responsabilidad es mantener el estado de la aplicación: preferencias del cliente (presupuesto, uso), lista de PDFs, fuentes web y las recomendaciones/justificaciones generadas por la IA. 

Vista (vista.py): Se encarga exclusivamente de la representación gráfica y la captura de datos de entrada. Contiene la MainWindow y todos los cuadros de diálogo (QDialog). Define los layouts, estilos y widgets, pero no toma ninguna decisión lógica ni realiza inferencias. Solo expone los botones para que sean escuchados.
Controlador (controlador.py): Es el "cerebro" que une la Vista y el Modelo. La clase AdvisorController escucha los eventos de la vista (clics en botones). Cuando ocurre un evento, el controlador:
Lee los datos de la Vista y actualiza el Modelo.
Invoca el motor de inferencia (en este caso, el mock del LLM mediante simular_llm()).
Toma los nuevos datos procesados del Modelo y ordena a la Vista que abra las ventanas de resultados correspondientes.
Punto de entrada (main.py): Orquesta la aplicación instanciando el Modelo, la Vista, pasándoselos al Controlador, aplicando la hoja de estilos global (QSS) y lanzando el bucle de eventos de la aplicación.
4. Explicación del modo Local/Web y cómo se refleja en la UI
El sistema integra una gestión dual del conocimiento (Local y Web) que influye directamente en el comportamiento de la interfaz y las respuestas del LLM:
Reflejo en la UI Principal: En la ventana principal, el usuario cuenta con el panel "3. Base de Datos del Asesor (IA)", compuesto por dos RadioButtons:
Solo Manuales Aportados (Offline)
Buscar Benchmarks en Internet (Web + Local).
Comportamiento Modo Local (Offline): Si el usuario selecciona esta opción, el simulador LLM restringe su análisis de contexto a los manuales que el usuario haya subido en la ventana de "Gestión de PDFs". Si el usuario intenta hacer clic en el botón "Fuentes Web", el Controlador bloquea la acción desplegando un cuadro de alerta (QMessageBox.warning) indicando que el asesor está en modo Offline y no se ha usado Internet.
Comportamiento Modo Web: Si se activa esta opción, el LLM asume que puede extraer información externa. En la UI, esto se refleja de dos maneras:
Al consultar la "Explicación Técnica", el texto de justificación incluye referencias a que los datos han sido cruzados con información actualizada de Internet.
El botón de "Fuentes Web" queda habilitado, abriendo un QDialog interactivo que muestra una tabla estructurada (Título, URL, Fecha) con los portales tecnológicos concretos (ej. GamersNexus, Tom's Hardware) que el sistema ha "consultado" para justificar su recomendación.


