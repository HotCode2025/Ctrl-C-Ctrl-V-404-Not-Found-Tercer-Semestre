package domain;

public class Persona {

    private final int idPersona;
    private static int contadorPersonas;

    static {
        System.out.println("1. Bloque estatico de inicializacion");
        ++Persona.contadorPersonas;
    }

    {
        contadorPersonas++;
        System.out.println("2. Bloque de inicializacion de instancia");
        this.idPersona = Persona.contadorPersonas++;
    }

    public Persona() {
        System.out.println("3. Constructor");
    }

    public int getIdPersona() {
        return idPersona;
    }
}
