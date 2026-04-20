class Pelicula:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def __str__(self) -> str:
        return self.nombre