package Modelo;

public class Mesa extends Producto {
    private String dimensiones;

    public Mesa(String nombre, double precio, int stock, String dimensiones) {
        super(nombre, precio, stock);
        this.dimensiones = dimensiones;
    }

    public String getDimensiones() { return dimensiones; }

    @Override
    public String toString() {
        return "MESA | " + nombre + " | Precio: " + precio + "€ | Stock: " + stock + " | Dimensiones: " + dimensiones;
    }
}