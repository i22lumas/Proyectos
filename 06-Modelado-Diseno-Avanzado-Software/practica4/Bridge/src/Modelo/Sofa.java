package Modelo;

public class Sofa extends Producto {
    private int plazas;

    public Sofa(String nombre, double precio, int stock, int plazas) {
        super(nombre, precio, stock);
        this.plazas = plazas;
    }

    public int getPlazas() { return plazas; }

    @Override
    public String toString() {
        return "SOFÁ | " + nombre + " | Precio: " + precio + "€ | Stock: " + stock + " | Plazas: " + plazas;
    }
}