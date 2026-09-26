package Modelo;
import java.util.ArrayList;
import java.util.List;

public class EmpresaA implements Buscador {
    private List<Sofa> catalogo;

    public EmpresaA() {
        catalogo = new ArrayList<>();
        catalogo.add(new Sofa("Sofá Piel", 800.0, 5, 3));
        catalogo.add(new Sofa("Sofá Básico", 300.0, 10, 2));
    }

    @Override
    public List<Producto> buscarPrecio() {
        return new ArrayList<>(catalogo);
    }

    @Override
    public List<Producto> buscarStock() {
        List<Producto> enStock = new ArrayList<>();
        for (Sofa s : catalogo) {
            if (s.getStock() > 0) {
                enStock.add(s);
            }
        }
        return enStock;
    }

    @Override
    public List<Producto> buscarDimensiones(String dimension) {
        // No vende mesas, devuelve lista vacía
        return new ArrayList<>(); 
    }

    @Override
    public List<Producto> buscarPlaza(int plazas) {
        List<Producto> resultado = new ArrayList<>();
        for (Sofa s : catalogo) {
            if (s.getPlazas() == plazas) {
                resultado.add(s);
            }
        }
        return resultado;
    }
}