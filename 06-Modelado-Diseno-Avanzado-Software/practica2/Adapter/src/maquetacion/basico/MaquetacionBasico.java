package maquetacion.basico;

import java.io.File;        
import java.io.FileReader;   
import java.io.FileWriter;   
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class MaquetacionBasico {

    
    //Añadir texto (String) al final de un archivo
    
    public void añadir(String texto, File archivo) throws IOException {
        try (FileWriter fw = new FileWriter(archivo, true); //Si append es true, añade al final del documento en vez de sobreescribir
            BufferedWriter bw = new BufferedWriter(fw)) {
            bw.write(texto);
            bw.newLine();
        }
    }

     //Extraer un párrafo indicando línea de inicio y fin.
    
    public String extraer(int inicio, int fin, File archivo) throws IOException {
        StringBuilder parrafo = new StringBuilder(); // Con StingBuilder concatenamos las lineas del parrafo
        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) { // 
            String linea;
            int numeroLinea = 1;

            while ((linea = br.readLine()) != null && numeroLinea <= fin) {
                if (numeroLinea >= inicio) {
                    parrafo.append(linea).append(System.lineSeparator());
                }
                numeroLinea++;
            }
        }
        return parrafo.toString().trim(); //con trim eliminamos el salto de línea final sobrante
    }

    //Dividir un fichero de texto en dos según una línea 
    public void dividir(int numeroLinea, File archivo) throws IOException {
        List<String> todasLasLineas = leerLineas(archivo);
        
        // Generar nombres para los nuevos ficheros 
        String path = archivo.getParent();
        String nombre = archivo.getName();
        File parte1 = new File(path, "parte1_" + nombre);
        File parte2 = new File(path, "parte2_" + nombre);

        escribirLineas(parte1, todasLasLineas.subList(0, Math.min(numeroLinea, todasLasLineas.size())));
        escribirLineas(parte2, todasLasLineas.subList(Math.min(numeroLinea, todasLasLineas.size()), todasLasLineas.size()));
    }

    // Métodos privados de apoyo
    
    private List<String> leerLineas(File archivo) throws IOException {
        List<String> lineas = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String l;
            while ((l = br.readLine()) != null) {
                lineas.add(l);
            }
        }
        return lineas;
    }

    private void escribirLineas(File archivo, List<String> lineas) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(archivo))) {
            for (String s : lineas) {
                bw.write(s);
                bw.newLine();
            }
        }
    }
}