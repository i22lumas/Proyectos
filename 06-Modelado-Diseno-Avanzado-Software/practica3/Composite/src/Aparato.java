public class Aparato extends Espacio {

    private String nombre;
    private double consumoPorHora;
    private double horasEstimadas;

    public Aparato(String nombre, double consumo, double horas)
    {
        this.nombre = nombre;
        this.consumoPorHora = consumo;
        this.horasEstimadas = horas;
    }

    @Override
    public String getNombre() {
        return this.nombre;
    }

     @Override public double calcularCosteHora() {
        return this.consumoPorHora;
    }

    @Override public double calcularHorasUso() {
        return this.horasEstimadas;
    }


}
