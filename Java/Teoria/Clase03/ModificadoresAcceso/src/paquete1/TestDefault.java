package paquete1;

import paquete2.Clase4;

public class TestDefault {
    public static void main(String[] args) {
        ClaseHija2 claseHija2 = new ClaseHija2();
        claseHija2.atributoDefault = "Cambio desde la prueba default";
        System.out.println("claseHija2 atributo default= " + claseHija2.atributoDefault);

        Clase4 clase4 = new Clase4("Publico");
        System.out.println("Atributo privado clase4 = " + clase4.getAtributoPrivate());
        clase4.setAtributoPrivate("Cambio atributo privado");
        //clase4.getAtributoPrivate();
        System.out.println("clase4 = " + clase4.getAtributoPrivate());
    }
}
