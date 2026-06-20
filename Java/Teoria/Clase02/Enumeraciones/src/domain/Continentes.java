package domain;

public enum Continentes {
    AFRICA(53, "1.2 billones"), 
    AMERICA(34, "3 billones"), 
    ASIA(44, "4 billones"), 
    EUROPA(36, "5 billones"), 
    OCEANIA(14, "6 billones");

    private final int paises;
    private final String habitantes;

    Continentes(int paises, String habitantes){
        this.paises = paises;
        this.habitantes = habitantes;
    }

    //Metedo GET

    public int getPaises () {
        return this.paises;
    }
    public String getHabitantes () {
        return this.habitantes;
    }
}
