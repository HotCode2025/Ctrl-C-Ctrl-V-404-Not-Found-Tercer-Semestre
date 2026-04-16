package ar.com.system2026.AlgoritmoDeBloque;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas = 0; // Reemplazo del bloque static

    // Constructor: aquí metemos la lógica que estaba en el bloque no estático
    public Persona() {
        this.idPersona = ++Persona.contadorPersonas;
        System.out.println("ID asignado desde el constructor: " + idPersona);
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
}