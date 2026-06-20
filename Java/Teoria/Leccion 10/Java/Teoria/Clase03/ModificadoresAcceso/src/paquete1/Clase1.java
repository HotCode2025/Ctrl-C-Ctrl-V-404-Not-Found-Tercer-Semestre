package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "valor atributo protegido";

    public Clase1() {
        System.out.println("Constructor publico");
    }

    protected Clase1(String atributoPublic) {
        System.out.println("Constructor protected");
    }

    public void metodoPublico() {
        System.out.println("Metodo publico");
    }

    protected void metodoProtected() {
        System.out.println("Metodo protected");
    }
}
