package maquetacion.avanzado;

import maquetacion.basico.MaquetacionBasico;
import java.io.File;
import java.io.IOException;

public class MaquetacionAdaptador implements MaquetacionAvanzada {
    
    private MaquetacionBasico basico;

    public MaquetacionAdaptador(MaquetacionBasico basico) {
        this.basico = basico;
    }

    @Override
    public void unir(File f1, File f2) throws IOException {
        String contenidoF2 = basico.extraer(1, 100000, f2);
        basico.añadir(contenidoF2, f1);
    }

    @Override
    public void combinar(File f1, File f2, int[] inicios, int[] fines) throws IOException {
        File resultado = new File("combinado.txt");
        
        //Con este bucle intercalmos los parrafos
        for (int i = 0; i < inicios.length; i++) {
            // Párrafo del fichero 1
            String p1 = basico.extraer(inicios[i], fines[i], f1);
            basico.añadir(p1, resultado);
            
            // Párrafo del fichero 2
            String p2 = basico.extraer(inicios[i], fines[i], f2);
            basico.añadir(p2, resultado);
        }
    }

    @Override
    public void separar(File archivo, int... lineasCorte) throws IOException {
        for (int corte : lineasCorte) {
            basico.dividir(corte, archivo);
        }
    }
}