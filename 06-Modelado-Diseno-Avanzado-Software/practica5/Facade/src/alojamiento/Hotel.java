package alojamiento;

import java.util.ArrayList;
import java.util.List;

public class Hotel {
    private String ciudad;
    private String fechaInicio;
    private String fechaFin;
    private int numeroPersonas;
    private boolean todoIncluido;

    private static List<Hotel> catalogo = new ArrayList<>();

    public Hotel(String ciudad, String fechaInicio, String fechaFin, int numeroPersonas, boolean todoIncluido) {
        this.ciudad = ciudad;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
        this.numeroPersonas = numeroPersonas;
        this.todoIncluido = todoIncluido;
    }

    public Hotel() {
        if (catalogo.isEmpty()) {
            catalogo.add(new Hotel("Córdoba", "15-05-2026", "22-05-2026", 2, true));
        }
    }

    public void buscarHotel(String ciudad, String fechaInicio, String fechaFin) {
        boolean encontrado = false;
        for (Hotel h : catalogo) {
            if (h.ciudad.equalsIgnoreCase(ciudad) && h.fechaInicio.equals(fechaInicio) && h.fechaFin.equals(fechaFin)) {
                System.out.println("Hotel en " + h.ciudad + " para " + h.numeroPersonas + " personas. Todo incluido: " + h.todoIncluido);
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay hoteles en " + ciudad + " para esas fechas.");
    }
}