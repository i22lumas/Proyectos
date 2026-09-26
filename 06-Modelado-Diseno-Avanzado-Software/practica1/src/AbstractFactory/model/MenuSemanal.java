package AbstractFactory.model;

public class MenuSemanal extends Menu {
        @Override
        public float calcularPrecio(){
            float precioTotal=0;
            for (Plato plato : platos)
            {
                precioTotal+=plato.getPrecio();
            }
            return precioTotal;
        }

}
