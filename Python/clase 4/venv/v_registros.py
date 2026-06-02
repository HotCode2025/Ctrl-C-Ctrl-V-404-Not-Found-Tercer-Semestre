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
        sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
        entrada = input("Ingrese las llaves primarias separadas por comas: ")
        llaves_primarias = tuple(entrada.split(","))
        cursor.execute(sentencia, (llaves_primarias,))
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()