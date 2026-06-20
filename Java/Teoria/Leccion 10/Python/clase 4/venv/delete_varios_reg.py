import psycopg2 

conexion = psycopg2.connect(
    host="localhost",
    port="5432",
    database="test_bd",
    user="postgres",
    password="ste"
)

try:
    with conexion:
      with conexion.cursor() as cursor:
        sentencia = "DELETE FROM persona WHERE id_persona IN %s"
        entrada = input("Ingrese los IDs de las personas a eliminar (separados por coma): ")
        valores = (tuple(entrada.split(",")),)
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Registros eliminados: {registros_eliminados}")

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()