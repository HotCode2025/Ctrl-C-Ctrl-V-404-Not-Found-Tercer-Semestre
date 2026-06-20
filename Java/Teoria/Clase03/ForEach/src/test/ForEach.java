package test;

import domain.Persona;

public class ForEach {
    public static void main(String[] args) {
        int edades[] = {10, 20, 30, 40, 50};

        System.out.println("ForEach con arreglo:");
        for (int edad : edades) {
            System.out.println("edad: " + edad);
        }

        Persona personas[] = {new Persona("Juan"), new Persona("Carla"), new Persona("Akira"), };

        for(Persona persona: personas) {
            System.out.println("persona = " + persona);
        }
    }
}
