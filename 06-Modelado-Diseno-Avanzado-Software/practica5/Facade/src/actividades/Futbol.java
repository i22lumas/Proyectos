package actividades;

import java.util.ArrayList;
import java.util.List;

public class Futbol {
    private int numeroPersonas;
    private String fecha;
    private String campo;
    private String localizacion;

    private static List<Futbol> catalogo = new ArrayList<>();

    public Futbol(int numeroPersonas, String fecha, String campo, String localizacion) {
        this.numeroPersonas = numeroPersonas;
        this.fecha = fecha;
        this.campo = campo;
        this.localizacion = localizacion;
    }

    public Futbol() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Futbol(22, "17-05-2026", "Campo Norte", "Córdoba"));
        }
    }

    public void buscarFutbol(String localizacion, String fecha) {
        boolean encontrado = false;
        for (Futbol f : catalogo) {
            if (f.localizacion.contains(localizacion) && f.fecha.equals(fecha)) {
                System.out.println("Fútbol en " + f.campo + " (" + f.localizacion + ")" + " - Aforo máximo: " + f.numeroPersonas + " personas");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay fútbol en " + localizacion + " el " + fecha);
    }
}