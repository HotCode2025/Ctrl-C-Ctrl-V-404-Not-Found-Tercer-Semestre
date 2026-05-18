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
        sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
        valores = ('Juan', 'Perez', 'juan.perez@example.com', 1)
        cursor.execute(sentencia, valores)
        registros_actualizados = cursor.rowcount
        print(f"Registros actualizados: {registros_actualizados}")

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()