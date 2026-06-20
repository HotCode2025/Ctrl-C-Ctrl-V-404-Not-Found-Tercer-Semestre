import java.util.Scanner;

public class CalculadoraUTN {
    static void main() {
        Scanner entrada = new Scanner(System.in);
        while (true) { //ciclo infinito
            System.out.println("****** Aplicacion CalculadoraUTN ******");
            mostrarMenu();
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    ejecutarOperacion(operacion, entrada);
                } //Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto...");
                    break;
                } else {
                    System.out.println("Opcion erronea: " + operacion);
                }
                //imprimimos un salto de linea antes de repetir el menu
                System.out.println();
            }catch (Exception e) { //Fin del try comienzo del catch
                System.out.println("Operacion erronea: "+e.getMessage());
                System.out.println();
            }
        }//Fin while
    }//Fin main

    private static void mostrarMenu(){
        //Mostramos el menu
        System.out.println("""
                    1_ Suma
                    2_ Resta
                    3_ Multiplicacion
                    4_ Dividir
                    5_ Salir
                    """);
        System.out.print("Operacion a realizar?: ");
    }//Fin metodo mostrarMenu

    private static void ejecutarOperacion(int operacion, Scanner entrada) {
        System.out.print("Digite el valor para el operando1: ");
        var operando1 = Double.parseDouble(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        var operando2 = Double.parseDouble(entrada.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> { //suma
                resultado = operando1 + operando2;
                System.out.println("Resultado de la suma: " + resultado);
            }
            case 2 -> { //resta
                resultado = operando1 - operando2;
                System.out.println("Resultado de la resta: " + resultado);
            }
            case 3 -> { //multiplicacion
                resultado = operando1 * operando2;
                System.out.println("Resultado de la multiplicacion: " + resultado);
            }
            case 4 -> { //division
                resultado = operando1 / operando2;
                System.out.println("Resultado de la division: " + resultado);
            }
            default -> System.out.println("Opcion erronea: " + operacion);
        }//Fin switch
    }//Fin metodo ejecutarOperacion
}//Fin clase
