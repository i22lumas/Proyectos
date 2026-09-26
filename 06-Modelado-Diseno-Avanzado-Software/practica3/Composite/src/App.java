public class App {
    public static void main(String[] args) {
        // 1. Creamos aparatos individuales (Hojas del Composite)
        // Aparato(nombre, consumoPorHora, horasEstimadas)
        Aparato pc1 = new Aparato("PC Aula 1", 0.5, 10);
        Aparato proyector1 = new Aparato("Proyector Aula 1", 1.2, 5);
        Aparato maquinaVending = new Aparato("Máquina Vending Pasillo", 2.0, 24);
        
        // 2. Creamos una sala y añadimos aparatos
        EspacioComposite sala1 = new EspacioComposite("Aula de Informática 1");
        sala1.añadir(pc1);
        sala1.añadir(proyector1);
        
        // 3. Creamos un edificio y añadimos la sala y aparatos sueltos
        // El enunciado indica que puede haber aparatos fuera de las salas 
        EspacioComposite edificioEinstein = new EspacioComposite("Edificio Albert Einstein");
        edificioEinstein.añadir(sala1);
        edificioEinstein.añadir(maquinaVending);
        
        // 4. Creamos el Campus (Nivel superior)
        EspacioComposite campusRabanales = new EspacioComposite("Campus de Rabanales");
        campusRabanales.añadir(edificioEinstein);

        // 5. Mostrar resultados
        System.out.println("--- Informe de Gasto Energético ---");
        mostrarInfo(sala1);
        mostrarInfo(edificioEinstein);
        mostrarInfo(campusRabanales);
    }

    private static void mostrarInfo(Espacio e) {
        System.out.println("Espacio: " + e.getNombre());
        System.out.println("  - Horas totales de uso estimadas: " + e.calcularHorasUso() + " h");
        System.out.println("  - Coste total acumulado: " + e.calcularCosteHora() + " €");
        System.out.println("-----------------------------------");
    }
}