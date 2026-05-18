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
        sentencia = "DELETE FROM persona WHERE id_persona = %s"
        entrada = input("Ingrese el ID de la persona a eliminar: ")
        valores = (entrada,)
        cursor.execute(sentencia, valores)
        registros_eliminados = cursor.rowcount
        print(f"Registros eliminados: {registros_eliminados}")

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()