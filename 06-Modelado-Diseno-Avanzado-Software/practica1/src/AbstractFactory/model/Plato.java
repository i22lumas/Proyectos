package AbstractFactory.model;

import AbstractFactory.model.enums.TipoPlato;
import AbstractFactory.model.enums.TipoAcompanamiento;

public class Plato {
    private String nombre;
    private float precio;
    private TipoPlato tipo;
    private TipoAcompanamiento acompanante;

    public Plato(String nombre, float precio, TipoPlato tipo, TipoAcompanamiento acompanante) {
        this.nombre = nombre;
        this.precio = precio;
        this.tipo = tipo;
        this.acompanante = acompanante;
    }

    public String getNombre() { 
        return nombre; 
    }

    public TipoPlato getTipo() {
        return tipo;
    }

    public TipoAcompanamiento getAcompanante() {
        return acompanante;
    }

    public float getPrecio() { return precio; }
}