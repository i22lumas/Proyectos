package AbstractFactory.factory;

import AbstractFactory.model.MenuSemanal;
import AbstractFactory.model.MenuTemporada;
import AbstractFactory.model.Plato;
import AbstractFactory.model.enums.TipoAcompanamiento;
import AbstractFactory.model.enums.TipoPlato;

public class FactoriaRestaurante extends FactoriaAbstracta {

  @Override
public MenuSemanal crearMenuSemanal(TipoAcompanamiento acompanamiento) {
    MenuSemanal ms = new MenuSemanal();
    ms.asignarPlatos(new Plato("Ensalada", 5.0f, TipoPlato.PRIMERO, null));
    ms.asignarPlatos(new Plato("Filete", 12.0f, TipoPlato.SEGUNDO, acompanamiento));
    ms.asignarPlatos(new Plato("Tarta", 4.0f, TipoPlato.POSTRE, null));
    return ms;
}

@Override
public MenuTemporada crearMenuTemporada() {
    MenuTemporada mt = new MenuTemporada();
    mt.asignarPlatos(new Plato("Ensalada de temporada", 15.0f, TipoPlato.PRIMERO, null));
    return mt;
}
}