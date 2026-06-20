import psycopg2 as bd

conexion = bd.connect(
    host="localhost",
    port="5432",
    database="test_bd",
    user="postgres",
    password="ste"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
            valores = ("Clara", "Agua", "clara@example.com")
            cursor.execute(sentencia, valores)
            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = ("Mariaa", "Perezz", "maria.updated3@example.com", 12)
            cursor.execute(sentencia, valores)
            
except Exception as e:
    print(f"Error: {e}. Se ha realizado un rollback.")
finally:
    conexion.close()

print("Registro insertado")