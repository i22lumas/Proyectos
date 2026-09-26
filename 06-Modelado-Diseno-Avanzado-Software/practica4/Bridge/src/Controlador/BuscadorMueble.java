package Controlador;

import Modelo.Buscador;
import Modelo.Producto;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BuscadorMueble {
    protected List<Buscador> proveedores;

    public BuscadorMueble() {
        this.proveedores = new ArrayList<>();
    }

    public void agregarProveedor(Buscador proveedor) {
        this.proveedores.add(proveedor);
    }

    // Método general: busca todo el stock sin filtrar (Caso 1)
    public List<Producto> buscarPorPrecioAscendente() {
        List<Producto> todos = new ArrayList<>();
        
        for (Buscador proveedor : proveedores) {
            todos.addAll(proveedor.buscarStock());
        }
        todos.sort(Comparator.comparingDouble(Producto::getPrecio));
        return todos;
    }

    // Método general: agrupa el stock de todos los productos sin filtrar (Caso 1)
    public List<Producto> buscarPorStockDescendente() {
        Map<String, Producto> agregados = new HashMap<>();
        
        for (Buscador proveedor : proveedores) {
            for (Producto p : proveedor.buscarStock()) {
                if (agregados.containsKey(p.getNombre())) {
                    Producto existente = agregados.get(p.getNombre());
                    existente.setStock(existente.getStock() + p.getStock());
                } else {
                    agregados.put(p.getNombre(), p);
                }
            }
        }
        List<Producto> resultado = new ArrayList<>(agregados.values());
        resultado.sort((p1, p2) -> Integer.compare(p2.getStock(), p1.getStock()));
        return resultado;
    }
}