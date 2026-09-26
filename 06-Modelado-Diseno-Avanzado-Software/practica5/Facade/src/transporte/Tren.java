package transporte;

import java.util.ArrayList;
import java.util.List;

public class Tren {
    private String ciudadOrigen;
    private String ciudadDestino;
    private int vagon;

    private static List<Tren> catalogo = new ArrayList<>();

    public Tren(String ciudadOrigen, String ciudadDestino, int vagon) {
        this.ciudadOrigen = ciudadOrigen;
        this.ciudadDestino = ciudadDestino;
        this.vagon = vagon;
    }

    public Tren() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Tren("Madrid", "Córdoba", 4));
            catalogo.add(new Tren("Sevilla", "Córdoba", 2));
        }
    }

    public void buscarTren(String ciudadOrigen, String ciudadDestino) {
        boolean encontrado = false;
        for (Tren t : catalogo) {
            if (t.ciudadOrigen.equalsIgnoreCase(ciudadOrigen) && t.ciudadDestino.equalsIgnoreCase(ciudadDestino)) {
                System.out.println("Tren: " + t.ciudadOrigen + " -> " + t.ciudadDestino + " (Vagón: " + t.vagon + ")");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay trenes de " + ciudadOrigen + " a " + ciudadDestino);
    }
}