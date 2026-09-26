import java.util.ArrayList;
import java.util.List;

public class EspacioComposite extends Espacio {

    private String nombre;
    private List<Espacio> componentes= new ArrayList<>();

    public EspacioComposite(String nombre) {
        this.nombre = nombre;
    }

    public void añadir(Espacio e){
        componentes.add(e);
    }

    @Override public String getNombre() {
        return this.nombre;
    }

    @Override public double calcularHorasUso() {
    
        double total=0;
        for(Espacio e:componentes){
            total+=e.calcularHorasUso();
        }
        return total;
    }

    @Override public double calcularCosteHora() {
        double totalCoste=0;
        for(Espacio e:componentes){
            //Si es aparato, susmamos su coste total (consumo*horas)
            if(e instanceof Aparato)
            {
                Aparato a = (Aparato) e;
                totalCoste+=a.calcularCosteHora()*a.calcularHorasUso();
            }
            else
            {
                //Si es una sala o un edificio, sumamos el coste que el ya habiía acumulado
                totalCoste+=e.calcularCosteHora();
            }
        }
        return totalCoste;
    }
}
