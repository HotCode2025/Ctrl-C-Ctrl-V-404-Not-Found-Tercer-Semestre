package test;

import domain.Persona;

public class BloquesInicializacion {
    public static void main(String[] args) {
        System.out.println("--- Primera instancia ---");
        Persona Persona1 = new Persona();

        System.out.println("\n--- Segunda instancia ---");
        Persona Persona2 = new Persona();

        System.out.println("\nId Persona1: " + Persona1.getIdPersona());
        System.out.println("Id Persona2: " + Persona2.getIdPersona());
    }
}
