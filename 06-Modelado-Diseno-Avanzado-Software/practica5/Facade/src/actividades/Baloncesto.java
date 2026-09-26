package actividades;

import java.util.ArrayList;
import java.util.List;

public class Baloncesto {
    private int numeroPersonas;
    private String fecha;
    private String pista;
    private String localizacion;

    private static List<Baloncesto> catalogo = new ArrayList<>();

    public Baloncesto(int numeroPersonas, String fecha, String pista, String localizacion) {
        this.numeroPersonas = numeroPersonas;
        this.fecha = fecha;
        this.pista = pista;
        this.localizacion = localizacion;
    }

    public Baloncesto() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Baloncesto(10, "15-05-2026", "Pabellón Sur", "Córdoba"));
        }
    }

    public void buscarBaloncesto(String localizacion, String fecha) {
        boolean encontrado = false;
        for (Baloncesto b : catalogo) {
            if (b.localizacion.contains(localizacion) && b.fecha.equals(fecha)) {
                System.out.println("Baloncesto en " + b.pista + " (" + b.localizacion + ")" + " - Jugadores: " + b.numeroPersonas);
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay baloncesto en " + localizacion + " el " + fecha);
    }
}