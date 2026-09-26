package AbstractFactory.model;
import java.util.List;
import java.util.ArrayList;

public abstract class Menu {
  protected List<Plato> platos= new ArrayList<>();

  public abstract float calcularPrecio();

  public List<Plato> getPlatos() {
    return platos;
  }

  public void asignarPlatos(Plato plato) {
    this.platos.add(plato);
  }
}