import psycopg2 #para conectarnos a posgresql
#Aca vamos a utlizar el fetchall para varios registros, utilizando la palabra IN
conexion = psycopg2.connect(
    user= 'postgres',
    password= 'Admin',
    host= '127.0.0.1',
    port= '5432',
    database= 'test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ("Juan", "Perez", "juanperez@mail.com", 4),
                ("Romina", "Ayala", "romiayala@mail.com", 5)
            )#es una tupla de tuplas
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount#
            print(f'Los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()