package Modelo;
import java.util.ArrayList;
import java.util.List;

public class EmpresaC implements Buscador {
    private List<Producto> catalogo;

    public EmpresaC() {
        catalogo = new ArrayList<>();
        catalogo.add(new Mesa("Mesa Cristal", 200.0, 2, "150x90"));
        catalogo.add(new Sofa("Sofá Cama", 450.0, 3, 2));
    }

    @Override
    public List<Producto> buscarPrecio() {
        return new ArrayList<>(catalogo);
    }

    @Override
    public List<Producto> buscarStock() {
        List<Producto> enStock = new ArrayList<>();
        for (Producto p : catalogo) {
            if (p.getStock() > 0) {
                enStock.add(p);
            }
        }
        return enStock;
    }

    @Override
    public List<Producto> buscarDimensiones(String dimension) {
        List<Producto> resultado = new ArrayList<>();
        for (Producto p : catalogo) {
            // Verificamos si es una instancia de Mesa para evitar errores
            if (p instanceof Mesa && ((Mesa) p).getDimensiones().equals(dimension)) {
                resultado.add(p);
            }
        }
        return resultado;
    }

    @Override
    public List<Producto> buscarPlaza(int plazas) {
        List<Producto> resultado = new ArrayList<>();
        for (Producto p : catalogo) {
            // Verificamos si es una instancia de Sofa
            if (p instanceof Sofa && ((Sofa) p).getPlazas() == plazas) {
                resultado.add(p);
            }
        }
        return resultado;
    }
}