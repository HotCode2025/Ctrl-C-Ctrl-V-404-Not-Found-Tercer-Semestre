import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "=" * 50)
    print(" SISTEMA DE CATÁLOGO DE PELÍCULAS")
    print("=" * 50)
    print("1️  Agregar película")
    print("2️  Listar películas")
    print("3️  Eliminar archivo de películas")
    print("4️  Salir")
    print("=" * 50)

def agregar_pelicula_interactivo():
    print("\n📝 AGREGAR NUEVA PELÍCULA")
    nombre = input("Ingrese el nombre de la película: ").strip()
    
    if nombre:
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    else:
        print(" El nombre de la película no puede estar vacío.")

def listar_peliculas_interactivo():

    print("\n LISTANDO CATÁLOGO")
    CatalogoPeliculas.listar_peliculas()

def eliminar_archivo_interactivo():

    print("\n ELIMINAR ARCHIVO")
    confirmar = input("¿Está seguro que desea eliminar el archivo de películas? (s/n): ").strip().lower()
    
    if confirmar == 's':
        CatalogoPeliculas.eliminar_archivo()
    else:
        print(" Operación cancelada.")

def main():

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            agregar_pelicula_interactivo()
        elif opcion == '2':
            listar_peliculas_interactivo()
        elif opcion == '3':
            eliminar_archivo_interactivo()
        elif opcion == '4':
            print("\n ¡Gracias por usar el catálogo de películas! Hasta luego.")
            break
        else:
            print("\n Opción no válida. Por favor, seleccione una opción entre 1 y 4.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()