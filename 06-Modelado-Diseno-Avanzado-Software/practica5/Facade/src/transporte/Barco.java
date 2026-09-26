package transporte;

import java.util.ArrayList;
import java.util.List;

public class Barco {
    private String ciudadOrigen;
    private String ciudadDestino;
    private String camerino;

    private static List<Barco> catalogo = new ArrayList<>();

    public Barco(String ciudadOrigen, String ciudadDestino, String camerino) {
        this.ciudadOrigen = ciudadOrigen;
        this.ciudadDestino = ciudadDestino;
        this.camerino = camerino;
    }

    public Barco() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Barco("Málaga", "Melilla", "Doble con ventana"));
        }
    }

    public void buscarBarco(String ciudadOrigen, String ciudadDestino) {
        boolean encontrado = false;
        for (Barco b : catalogo) {
            if (b.ciudadOrigen.equalsIgnoreCase(ciudadOrigen) && b.ciudadDestino.equalsIgnoreCase(ciudadDestino)) {
                System.out.println("Barco: " + b.ciudadOrigen + " -> " + b.ciudadDestino + " (Camerino: " + b.camerino + ")");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay barcos de " + ciudadOrigen + " a " + ciudadDestino);
    }
}