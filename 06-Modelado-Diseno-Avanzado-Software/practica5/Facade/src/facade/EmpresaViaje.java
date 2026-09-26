package facade;

import transporte.*;
import alojamiento.*;
import actividades.*;

public class EmpresaViaje {
    private Avion avion = new Avion();
    private Barco barco = new Barco();
    private Tren tren = new Tren();

    private Hotel hotel = new Hotel();
    private Hostal hostal = new Hostal();
    private ApartamentoTuristico apartamento = new ApartamentoTuristico();

    private Patinaje patinaje = new Patinaje();
    private Futbol futbol = new Futbol();
    private Baloncesto baloncesto = new Baloncesto();

    // Modificamos el método para que reciba el tipo y filtre
    private void buscarTransporte(String ciudadOrigen, String ciudadDestino, String tipoTransporte) {
        System.out.println("\n--- 1. Buscando Opciones de Transporte: " + tipoTransporte.toUpperCase() + " ---");
        if (tipoTransporte.equalsIgnoreCase("Avion")) {
            avion.buscarAvion(ciudadOrigen, ciudadDestino);
        } else if (tipoTransporte.equalsIgnoreCase("Barco")) {
            barco.buscarBarco(ciudadOrigen, ciudadDestino);
        } else if (tipoTransporte.equalsIgnoreCase("Tren")) {
            tren.buscarTren(ciudadOrigen, ciudadDestino);
        } else {
            System.out.println("Tipo de transporte no válido.");
        }
    }

    // Modificamos el método para que reciba el tipo y filtre
    private void buscarAlojamiento(String ciudad, String fechaInicio, String fechaFin, String tipoAlojamiento) {
        System.out.println("\n--- 2. Buscando Opciones de Alojamiento: " + tipoAlojamiento.toUpperCase() + " ---");
        if (tipoAlojamiento.equalsIgnoreCase("Hotel")) {
            hotel.buscarHotel(ciudad, fechaInicio, fechaFin);
        } else if (tipoAlojamiento.equalsIgnoreCase("Hostal")) {
            hostal.buscarHostal(ciudad, fechaInicio, fechaFin);
        } else if (tipoAlojamiento.equalsIgnoreCase("Apartamento")) {
            apartamento.buscarApartamentoTuristico(ciudad, fechaInicio, fechaFin);
        } else {
            System.out.println("Tipo de alojamiento no válido.");
        }
    }

    // Las actividades se mantienen igual, buscando todo lo disponible en el destino
    private void buscarActividades(String localizacion, String fecha) {
        System.out.println("\n--- 3. Buscando Actividades Culturales/Deportivas ---");
        patinaje.buscarPatinaje(localizacion, fecha);
        futbol.buscarFutbol(localizacion, fecha);
        baloncesto.buscarBaloncesto(localizacion, fecha);
    }

    public void organizarViaje(String origen, String destino, String fechaInicio, String fechaFin, String tipoTransporte, String tipoAlojamiento) {
        System.out.println("Iniciando la planificación del viaje: " + origen + " -> " + destino);
        System.out.println("Fechas: del " + fechaInicio + " al " + fechaFin);
        
        // Pasamos las preferencias del cliente a los métodos internos
        buscarTransporte(origen, destino, tipoTransporte);
        buscarAlojamiento(destino, fechaInicio, fechaFin, tipoAlojamiento);
        
        // Para las actividades, usamos el destino y la fecha de inicio
        buscarActividades(destino, fechaInicio); 
    }
}