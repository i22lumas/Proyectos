package alojamiento;

import java.util.ArrayList;
import java.util.List;

public class Hostal {
    private String ciudad;
    private String fechaInicio;
    private String fechaFin;
    private int numeroPersonas;

    private static List<Hostal> catalogo = new ArrayList<>();

    public Hostal(String ciudad, String fechaInicio, String fechaFin, int numeroPersonas) {
        this.ciudad = ciudad;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
        this.numeroPersonas = numeroPersonas;
    }

    public Hostal() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Hostal("Córdoba", "15-05-2026", "22-05-2026", 4));
        }
    }

    public void buscarHostal(String ciudad, String fechaInicio, String fechaFin) {
        boolean encontrado = false;
        for (Hostal h : catalogo) {
            if (h.ciudad.equalsIgnoreCase(ciudad) && h.fechaInicio.equals(fechaInicio) && h.fechaFin.equals(fechaFin)) {
                System.out.println("Hostal en " + h.ciudad + " para " + h.numeroPersonas + " personas.");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay hostales en " + ciudad + " para esas fechas.");
    }
}