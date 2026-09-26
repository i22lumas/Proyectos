import facade.EmpresaViaje;

public class Cliente {
    public static void main(String[] args) {
        // 1. Instanciamos la fachada
        EmpresaViaje agencia = new EmpresaViaje();
        
        String miOrigen = "Madrid";
        String miDestino = "Córdoba";
        String miFechaInicio = "15-05-2026";
        String miFechaFin = "22-05-2026";
        String tipoTransporte = "Avion"; 
        String tipoAlojamiento = "Hotel"; 
        
        System.out.println("==================================================");
        System.out.println("   SOLICITANDO BÚSQUEDA DE VIAJE");
        System.out.println("==================================================");
        
        agencia.organizarViaje(miOrigen, miDestino, miFechaInicio, miFechaFin, tipoTransporte, tipoAlojamiento);
    }
}