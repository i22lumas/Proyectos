package AbstractFactory.factory;

import AbstractFactory.model.Menu;
import AbstractFactory.model.enums.TipoAcompanamiento;

public abstract class FactoriaAbstracta{

    //Metodos a implementar en las factorias concretas
    public abstract Menu crearMenuSemanal (TipoAcompanamiento acompanamiento);
    public abstract Menu crearMenuTemporada ();
    
}
