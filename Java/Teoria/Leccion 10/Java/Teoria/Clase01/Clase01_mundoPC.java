
package mundoPc;
//coloco asterisco y se importan todas las clases del paquete y no es necesario importat una por una
import ar.com.system2026.mundopc.*;

public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 15);//importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
    
        //Creamos otros objetos
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        Monitor monitorEscritorio = new Monitor("Escritorio", 32);
        Teclado tecladoEscritorio = new Teclado("Bluetooth", "Escritorio");
        Raton ratonEscritorio = new Raton("Bluetooth", "Escritorio");
        Computadora computadoraEscritorio = new Computadora("Computadora Escritorio", monitorEscritorio, tecladoEscritorio, ratonEscritorio);
        
        Monitor monitorOficina = new Monitor("Oficina", 32);
        Teclado tecladoOficina = new Teclado("Bluetooth", "Oficina");
        Raton ratonOficina = new Raton("Bluetooth", "Oficina");
        Computadora computadoraOficina = new Computadora("Computadora Oficina", monitorOficina, tecladoOficina, ratonOficina);
       
        Computadora compu4 = new Computadora("Computadora Lenovo", new Monitor("Lenovo", 15), new Teclado("Inalambrico", "Lenovo"), new Raton("Inalambrico", "Lenovo"));
        Computadora compu5 = new Computadora("Computadora Apple", new Monitor("Apple", 27), new Teclado("USB", "Apple"), new Raton("USB", "Apple"));
        Computadora compu6 = new Computadora("Computadora Samsung", new Monitor("Samsung", 34), new Teclado("Inalambrico", "Samsung"), new Raton("Inalambrico", "Samsung"));
        Computadora compu7 = new Computadora("Computadora Sony", new Monitor("Sony", 24), new Teclado("Bluetooth", "Sony"), new Raton("Bluetooth", "Sony"));
        Computadora compu8 = new Computadora("Computadora Acer", new Monitor("Acer", 21), new Teclado("USB", "Acer"), new Raton("USB", "Acer"));
        Computadora compu9 = new Computadora("Computadora Dell", new Monitor("Dell", 27), new Teclado("Bluetooth", "Dell"), new Raton("Bluetooth", "Dell"));
        
        Orden orden1 = new Orden();//inicializamos el arreglo
        Orden orden2 = new Orden(); // nueva lista para el objeto orden2
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraOficina);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(compu7);
        orden1.agregarComputadora(compu4);
        orden1.agregarComputadora(compu5);
        orden1.agregarComputadora(compu6);
        orden1.agregarComputadora(compu7);
        orden1.agregarComputadora(compu8);
        orden1.agregarComputadora(compu9);
        orden1.agregarComputadora(compu4);
        
        
        
        
        Computadora computadoraVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonOficina);
        orden2.agregarComputadora(computadoraVarias);
       
        orden1.mostarOrden();
        orden2.mostarOrden();
        
            
    }
}
//Crear mas objetos de tipo computadora con todos sus elementos
//Completar una lista en el objeto orden1 que llegue a los 10 elementos
//Probar de esta manera los metodos al maximo rendimiento
