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
    valores = ("Maria", "Perez", "maria@example.com")
    cursor.execute(sentencia, valores)
    conexion.commit()
    print("Registro insertado, pero no confirmado aún.")
except Exception as e:
    conexion.rollback()
    print(f"Error: {e}. Se ha realizado un rollback.")
finally:
    conexion.close()