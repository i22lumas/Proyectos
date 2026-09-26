package Controlador;

import Modelo.Buscador;
import Modelo.Mesa;
import Modelo.Producto;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BuscadorMesa extends BuscadorMueble {

    @Override
    public List<Producto> buscarPorPrecioAscendente() {
        List<Producto> mesas = new ArrayList<>();
        
        for (Buscador proveedor : proveedores) {
            for (Producto p : proveedor.buscarStock()) {
                // Filtramos estrictamente para que solo entren Mesas
                if (p instanceof Mesa) {
                    mesas.add(p);
                }
            }
        }
        mesas.sort(Comparator.comparingDouble(Producto::getPrecio));
        return mesas;
    }

    @Override
    public List<Producto> buscarPorStockDescendente() {
        Map<String, Producto> agregados = new HashMap<>();
        
        for (Buscador proveedor : proveedores) {
            for (Producto p : proveedor.buscarStock()) {
                if (p instanceof Mesa) {
                    if (agregados.containsKey(p.getNombre())) {
                        Producto existente = agregados.get(p.getNombre());
                        existente.setStock(existente.getStock() + p.getStock());
                    } else {
                        agregados.put(p.getNombre(), p);
                    }
                }
            }
        }
        List<Producto> resultado = new ArrayList<>(agregados.values());
        resultado.sort((p1, p2) -> Integer.compare(p2.getStock(), p1.getStock()));
        return resultado;
    }

    // Método específico definido en el diagrama UML
    public List<Producto> buscarDimensiones(String dimension) {
        List<Producto> resultado = new ArrayList<>();
        for (Buscador proveedor : proveedores) {
            resultado.addAll(proveedor.buscarDimensiones(dimension));
        }
        return resultado;
    }
}