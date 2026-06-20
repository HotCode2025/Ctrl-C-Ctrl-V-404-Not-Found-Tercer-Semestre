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
        sentencia = "SELECT * FROM persona WHERE id_persona = %s"
        id_persona = int(input("Ingrese el ID de la persona: "))
        cursor.execute(sentencia, (id_persona,))
        resultados = cursor.fetchone()
        print(resultados)

except Exception as e:
    print(f"Error: {e}")
finally:
    conexion.close()