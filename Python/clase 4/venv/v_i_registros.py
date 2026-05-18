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
        sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s) "
        valores = (
           ('Carlos', 'Gomez', 'carlos.gomez@example.com'),
           ('Ana', 'Lopez', 'ana.lopez@example.com'),
           ('Luis', 'Martinez', 'luis.martinez@example.com')
        )
        cursor.executemany(sentencia, valores) 
        registros_insertados = cursor.rowcount
        print(f"Registros insertados: {registros_insertados}")

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()