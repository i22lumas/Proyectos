package Modelo;
import java.util.List;

public interface Buscador {
    List<Producto> buscarPrecio();
    List<Producto> buscarStock();
    List<Producto> buscarDimensiones(String dimension);
    List<Producto> buscarPlaza(int plazas);
}