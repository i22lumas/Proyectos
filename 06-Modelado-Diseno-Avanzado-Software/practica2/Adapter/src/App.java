import maquetacion.basico.MaquetacionBasico;
import maquetacion.avanzado.MaquetacionAdaptador;
import maquetacion.avanzado.MaquetacionAvanzada;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;

public class App {
    public static void main(String[] args) {
        try {
            // 1. Preparar archivos de prueba (Simulando el entorno)
            File f1 = prepararArchivoPrueba("fichero1.txt", "F1: Linea 1\nF1: Linea 2\nF1: Linea 3\n");
            File f2 = prepararArchivoPrueba("fichero2.txt", "F2: Linea 1\nF2: Linea 2\nF2: Linea 3");

            // 2. Configuración del Patrón Adapter según el diagrama
            // Creamos el objeto existente (Adaptee)
            MaquetacionBasico maquetadorBasico = new MaquetacionBasico();
            
            // Creamos el adaptador pasándole el objeto básico y lo tratamos como la Interfaz Requerida
            MaquetacionAvanzada maquetadorAvanzado = new MaquetacionAdaptador(maquetadorBasico);

            System.out.println("--- PRUEBA SISTEMA DE MAQUETACIÓN AVANZADA ---");

            // 3. Prueba de UNIR
            System.out.println("\nEjecutando 'unir' (f2 al final de f1)...");
            maquetadorAvanzado.unir(f1, f2);
            imprimirArchivo(f1);

            // 4. Prueba de COMBINAR (Intercalar párrafos)
            System.out.println("\nEjecutando 'combinar' (Intercalando líneas 1 y 2 de cada archivo)...");
            int[] inicios = {1, 2};
            int[] fines = {1, 2};
            maquetadorAvanzado.combinar(f1, f2, inicios, fines);
            imprimirArchivo(new File("combinado.txt"));

            // 5. Prueba de SEPARAR
            System.out.println("\nEjecutando 'separar' (Corte en línea 2 del f2 original)...");
            maquetadorAvanzado.separar(f2, 2);
            System.out.println("Archivos generados: parte1_fichero2.txt y parte2_fichero2.txt");

        } catch (IOException e) {
            System.err.println("Error en la ejecución: " + e.getMessage());
        }
    }

    // Método auxiliar para crear archivos rápidamente
    private static File prepararArchivoPrueba(String nombre, String contenido) throws IOException {
        File archivo = new File(nombre);
        try (FileWriter fw = new FileWriter(archivo)) {
            fw.write(contenido);
        }
        return archivo;
    }

    // Método auxiliar para mostrar resultados por consola
    private static void imprimirArchivo(File archivo) throws IOException {
        System.out.println(">> Contenido de " + archivo.getName() + ":");
        Files.lines(archivo.toPath()).forEach(linea -> System.out.println("   " + linea));
    }
}