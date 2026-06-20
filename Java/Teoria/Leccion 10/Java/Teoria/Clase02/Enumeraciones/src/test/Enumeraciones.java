package test;

import domain.Continentes;
import domain.Dia;

public class Enumeraciones {
    public static void main(String[] args) {

/*         System.out.println("Dia 1: " + Dia.LUNES);
        indicarDiaSemana(Dia.LUNES);

        System.out.println("\nContinente: " + Continentes.AMERICA);
        indicarContinente(Continentes.AMERICA); */

        System.out.println("Contienente No 4: "+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to Contienente: "+Continentes.AMERICA.getPaises());
        System.out.println("No. de habitantes en el 4to Contienente: "+Continentes.AMERICA.getHabitantes());
    }

    private static void indicarDiaSemana(Dia dia) {
        switch (dia) {
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
            case MIERCOLES:
                System.out.println("Tercer dia de la semana");
            case JUEVES:
                System.out.println("Cuarto dia de la semana");
            case VIERNES:
                System.out.println("Quinto dia de la semana");
            case SABADO:
                System.out.println("Sexto dia de la semana");
            case DOMINGO:
                System.out.println("Septimo dia de la semana");
            default:
                break;
        }
    }

}
