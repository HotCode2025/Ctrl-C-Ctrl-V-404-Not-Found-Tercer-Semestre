import psycopg2 as bd

conexion = bd.connect(
    host="localhost",
    port="5432",
    database="test_bd",
    user="postgres",
    password="ste"
)

try:
    #conexion.autocommit = False #esto no debe hacerse, es mejor manejarlo con el bloque try-except
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    valores = ("Juana", "De Arco", "juana@example.com")
    cursor.execute(sentencia, valores)
    #sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
    #valores = ("Maria", "Perezz", "maria.updated@example.com", 12)
    #cursor.execute(sentencia, valores)
    conexion.commit()
    print("Registro insertado")
except Exception as e:
    conexion.rollback()
    print(f"Error: {e}. Se ha realizado un rollback.")
finally:
    conexion.close()