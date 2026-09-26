package maquetacion.avanzado;

import java.io.File;
import java.io.IOException;

public interface MaquetacionAvanzada {
    
    // Método para unir el contenido de f2 al final de f1
    void unir(File f1, File f2) throws IOException;

    // Método para extraer un trozo de f1 y f2 y juntarlos en un archivo nuevo
    // Recibe un array con todas las líneas de inicio, y otro con todas las líneas de fin
    void combinar(File f1, File f2, int[] inicios, int[] fines) throws IOException;

    // Método para dividir un archivo en varias partes según los puntos de corte
    // Nota: int... significa que puede recibir varios números separados por comas
    void separar(File archivo, int... puntosCorte) throws IOException;

}