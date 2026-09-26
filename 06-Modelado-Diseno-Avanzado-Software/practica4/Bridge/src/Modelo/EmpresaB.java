package Modelo;
import java.util.ArrayList;
import java.util.List;

public class EmpresaB implements Buscador {
    private List<Mesa> catalogo;

    public EmpresaB() {
        catalogo = new ArrayList<>();
        catalogo.add(new Mesa("Mesa Comedor", 150.0, 4, "120x80"));
        catalogo.add(new Mesa("Mesa Oficina", 120.0, 15, "100x60"));
    }

    @Override
    public List<Producto> buscarPrecio() {
        return new ArrayList<>(catalogo);
    }

    @Override
    public List<Producto> buscarStock() {
        List<Producto> enStock = new ArrayList<>();
        for (Mesa m : catalogo) {
            if (m.getStock() > 0) {
                enStock.add(m);
            }
        }
        return enStock;
    }

    @Override
    public List<Producto> buscarDimensiones(String dimension) {
        List<Producto> resultado = new ArrayList<>();
        for (Mesa m : catalogo) {
            if (m.getDimensiones().equals(dimension)) {
                resultado.add(m);
            }
        }
        return resultado;
    }

    @Override
    public List<Producto> buscarPlaza(int plazas) {
        // No vende sofás, devuelve lista vacía
        return new ArrayList<>(); 
    }
}