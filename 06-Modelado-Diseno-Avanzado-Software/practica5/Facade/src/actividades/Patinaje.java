package actividades;

import java.util.ArrayList;
import java.util.List;

public class Patinaje {
    private int numeroPersonas;
    private String fecha;
    private String monitor;
    private String localizacion;

    private static List<Patinaje> catalogo = new ArrayList<>();

    public Patinaje(int numeroPersonas, String fecha, String monitor, String localizacion) {
        this.numeroPersonas = numeroPersonas;
        this.fecha = fecha;
        this.monitor = monitor;
        this.localizacion = localizacion;
    }

    public Patinaje() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Patinaje(10, "16-05-2026", "Carlos", "Pista Central Córdoba"));
        }
    }

    public void buscarPatinaje(String localizacion, String fecha) {
        boolean encontrado = false;
        for (Patinaje p : catalogo) {
            if (p.localizacion.contains(localizacion) && p.fecha.equals(fecha)) {
                System.out.println("Patinaje en " + p.localizacion + " con el monitor " + p.monitor + " (Grupos de hasta: " + p.numeroPersonas + " personas)");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay patinaje en " + localizacion + " el " + fecha);
    }
}