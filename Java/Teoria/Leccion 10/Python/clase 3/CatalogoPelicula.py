import os


class CatalogoPelicula:
    ruta_archivo = 'peliculas.txt'

    @staticmethod
    def agregar_pelicula(pelicula) -> None:

        try:
            with open('peliculas.txt', 'a', encoding='utf-8') as archivo:
                archivo.write(pelicula.nombre + '\n')
            print(f"Película '{pelicula.nombre}' agregada correctamente.")
        except Exception as e:
            print(f"Error al agregar película: {e}")

    @staticmethod
    def listar_peliculas() -> None:

        try:
            if not os.path.exists('peliculas.txt'):
                print("No hay películas registradas. El archivo no existe.")
                return

            with open('peliculas.txt', 'r', encoding='utf-8') as archivo:
                peliculas = archivo.readlines()

            if not peliculas:
                print("El catálogo está vacío.")
                return

            print("\n" + "=" * 50)
            print("CATÁLOGO DE PELÍCULAS")
            print("=" * 50)
            for i, pelicula in enumerate(peliculas, 1):
                print(f"{i}. {pelicula.strip()}")
            print("=" * 50 + "\n")

        except Exception as e:
            print(f" Error al listar películas: {e}")

    @staticmethod
    def eliminar_archivo() -> None:

        try:
            if os.path.exists('peliculas.txt'):
                os.remove('peliculas.txt')
                print(f"Archivo '{'peliculas.txt'}' eliminado correctamente.")
            else:
                print(f"El archivo '{'peliculas.txt'}' no existe.")
        except Exception as e:
            print(f"Error al eliminar archivo: {e}")
