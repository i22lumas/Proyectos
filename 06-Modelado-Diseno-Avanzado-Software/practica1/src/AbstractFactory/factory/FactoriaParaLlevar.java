package AbstractFactory.factory;
import AbstractFactory.model.MenuSemanal;
import AbstractFactory.model.MenuTemporada;
import AbstractFactory.model.Plato;
import AbstractFactory.model.enums.TipoAcompanamiento;
import AbstractFactory.model.enums.TipoPlato;

public class FactoriaParaLlevar extends FactoriaAbstracta {
    
    //Para llevar tenemos que aplicar un recargo del 2%
    private float recargo = 1.02f;
    @Override
    public MenuSemanal crearMenuSemanal(TipoAcompanamiento acompanamiento) {
        MenuSemanal ms = new MenuSemanal();
        ms.asignarPlatos(new Plato("Ensalada", 5.0f*recargo, TipoPlato.PRIMERO, null));
        ms.asignarPlatos(new Plato("Filete", 12.0f*recargo, TipoPlato.SEGUNDO, acompanamiento));
        return ms;
    }

    @Override
    public MenuTemporada crearMenuTemporada() {
        MenuTemporada mt = new MenuTemporada();
        mt.asignarPlatos(new Plato("Ensalada de temporada", 15.0f*recargo, TipoPlato.PRIMERO, null));
        return mt;
    }
}
