package alojamiento;

import java.util.ArrayList;
import java.util.List;

public class ApartamentoTuristico {
    private String ciudad;
    private String fechaInicio;
    private String fechaFin;
    private int numeroPersonas;
    private String ubicacion;

    private static List<ApartamentoTuristico> catalogo = new ArrayList<>();

    public ApartamentoTuristico(String ciudad, String fechaInicio, String fechaFin, int numeroPersonas, String ubicacion) {
        this.ciudad = ciudad;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
        this.numeroPersonas = numeroPersonas;
        this.ubicacion = ubicacion;
    }

    public ApartamentoTuristico() {
        if (catalogo.isEmpty()) {
            catalogo.add(new ApartamentoTuristico("Córdoba", "15-05-2026", "22-05-2026", 6, "Centro histórico"));
        }
    }

    public void buscarApartamentoTuristico(String ciudad, String fechaInicio, String fechaFin) {
        boolean encontrado = false;
        for (ApartamentoTuristico a : catalogo) {
            if (a.ciudad.equalsIgnoreCase(ciudad) && a.fechaInicio.equals(fechaInicio) && a.fechaFin.equals(fechaFin)) {
                System.out.println("Apartamento en " + a.ubicacion + " (" + a.ciudad + ") para " + a.numeroPersonas + " personas.");
                encontrado = true;
            }
        }
        if (!encontrado) System.out.println("No hay apartamentos en " + ciudad + " para esas fechas.");
    }
}