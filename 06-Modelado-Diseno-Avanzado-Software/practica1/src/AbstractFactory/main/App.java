package AbstractFactory.main;

import AbstractFactory.factory.*;
import AbstractFactory.model.*;
import AbstractFactory.model.enums.TipoAcompanamiento;
import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        FactoriaAbstracta factoria = null;
        Menu miPedido = null;

        System.out.println("--- RESTAURANTE ---");
        System.out.println("Seleccione modo de consumo:");
        System.out.println("1. Restaurante");
        System.out.println("2. Para Llevar (+2%)");
        int modo = sc.nextInt();

        if (modo == 2) {
            factoria = new FactoriaParaLlevar();
        } else {
            factoria = new FactoriaRestaurante();
        }

        System.out.println("\nSeleccione el menú:");
        System.out.println("1. Menú Semanal (Requiere elegir acompañamiento)");
        System.out.println("2. Menú de Temporada");
        int tipo = sc.nextInt();

        if (tipo == 2) {
            miPedido = factoria.crearMenuTemporada();
        } else {
            System.out.println("\nElija acompañamiento para el plato principal:");
            System.out.println("1. Patatas Fritas");
            System.out.println("2. Ensalada");
            int aco = sc.nextInt();
            
            TipoAcompanamiento acompanamiento = (aco == 1) ? 
                TipoAcompanamiento.PATATAS_FRITAS : TipoAcompanamiento.ENSALADA;

            miPedido = factoria.crearMenuSemanal(acompanamiento);
        }

        // Mostrar Resultados
        System.out.println("\n========================================");
        System.out.println("          TICKET DE PEDIDO              ");
        System.out.println("========================================");
        
        // Listamos cada plato del menú
        for (Plato p : miPedido.getPlatos()) {
            // Mostramos el nombre del plato y su precio (que ya incluye el recargo si es para llevar)
            System.out.printf("- %-25s | Price: %.2f€\n", p.getNombre(), p.getPrecio());
        }

        System.out.println("----------------------------------------");
        
        // El método calcularPrecio suma los precios de la lista 'platos'
        float total = miPedido.calcularPrecio();
        
        System.out.printf("TOTAL A PAGAR:                %.2f€\n", total);
        System.out.println("========================================");
        
        sc.close();
    }
}