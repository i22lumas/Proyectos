package transporte;

import java.util.ArrayList;
import java.util.List;

public class Avion {
    private String ciudadOrigen;
    private String ciudadDestino;
    private double pesoEquipaje;

    // Creamos una lista estática para simular el catálogo de vuelos
    private static List<Avion> catalogoVuelos = new ArrayList<>();

    // Constructor con parámetros
    public Avion(String ciudadOrigen, String ciudadDestino, double pesoEquipaje) {
        this.ciudadOrigen = ciudadOrigen;
        this.ciudadDestino = ciudadDestino;
        this.pesoEquipaje = pesoEquipaje;
    }

    // Constructor vacío que la Fachada usa para inicializar el servicio
    public Avion() {
        // Llenamos el catálogo con algunos vuelos de prueba si está vacío
        if (catalogoVuelos.isEmpty()) {
            catalogoVuelos.add(new Avion("Madrid", "Córdoba", 20.0));
            catalogoVuelos.add(new Avion("Barcelona", "Córdoba", 15.0));
            catalogoVuelos.add(new Avion("Valencia", "Madrid", 25.0));
        }
    }

    public void buscarAvion(String ciudadOrigenBuscada, String ciudadDestinoBuscada) {
        boolean encontrado = false;
        
        for (Avion vuelo : catalogoVuelos) {
            if (vuelo.ciudadOrigen.equalsIgnoreCase(ciudadOrigenBuscada) && vuelo.ciudadDestino.equalsIgnoreCase(ciudadDestinoBuscada)) {
                
                System.out.println("Vuelo encontrado: " + vuelo.ciudadOrigen + " -> " + vuelo.ciudadDestino + " (Equipaje máx: " + vuelo.pesoEquipaje + "kg)");
                encontrado = true;
            }
        }
        
        if (!encontrado) {
            System.out.println("No se encontraron vuelos de " + ciudadOrigenBuscada + " a " + ciudadDestinoBuscada);
        }
    }
}