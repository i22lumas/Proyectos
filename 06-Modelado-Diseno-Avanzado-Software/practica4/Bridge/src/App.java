import Controlador.BuscadorMueble;
import Controlador.BuscadorMesa;
import Controlador.BuscadorSofa;
import Modelo.EmpresaA;
import Modelo.EmpresaB;
import Modelo.EmpresaC;

public class App {
    public static void main(String[] args) {
        // 1. Instanciamos las implementaciones concretas (Empresas)
        EmpresaA empresaA = new EmpresaA();
        EmpresaB empresaB = new EmpresaB();
        EmpresaC empresaC = new EmpresaC();

        System.out.println("==========================================================");
        System.out.println(" CASO 1: BÚSQUEDA GLOBAL (Cualquier producto)");
        System.out.println("==========================================================");
        
        BuscadorMueble buscadorGlobal = new BuscadorMueble();
        buscadorGlobal.agregarProveedor(empresaA);
        buscadorGlobal.agregarProveedor(empresaB);
        buscadorGlobal.agregarProveedor(empresaC);

        System.out.println("\n--- Ordenado por PRECIO ASCENDENTE ---");
        buscadorGlobal.buscarPorPrecioAscendente().forEach(System.out::println);

        System.out.println("\n--- Ordenado por STOCK DESCENDENTE (Agrupado) ---");
        buscadorGlobal.buscarPorStockDescendente().forEach(System.out::println);


        System.out.println("\n==========================================================");
        System.out.println(" CASO 2: BÚSQUEDA EXCLUSIVA DE MESAS");
        System.out.println("==========================================================");
        
        BuscadorMesa buscadorMesas = new BuscadorMesa();
        buscadorMesas.agregarProveedor(empresaB);
        buscadorMesas.agregarProveedor(empresaC);

        buscadorMesas.buscarPorPrecioAscendente().forEach(System.out::println);


        System.out.println("\n==========================================================");
        System.out.println(" CASO 3: BÚSQUEDA EXCLUSIVA DE SOFÁS");
        System.out.println("==========================================================");
        
        BuscadorSofa buscadorSofas = new BuscadorSofa();
        buscadorSofas.agregarProveedor(empresaA);
        buscadorSofas.agregarProveedor(empresaC);

        buscadorSofas.buscarPorStockDescendente().forEach(System.out::println);
    }
}