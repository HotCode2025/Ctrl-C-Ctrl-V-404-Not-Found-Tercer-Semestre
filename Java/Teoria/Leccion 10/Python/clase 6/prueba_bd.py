import psycopg2 #para conectarnos a posgresql

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
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Digite un numeropara el id_persona: ')
            cursor.execute(sentencia, (id_persona,))#de esta manera ejecutamos la sentencia
            registros = cursor.fetchone()#recupera todos los registros que seran una lista
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#https//www.psycopg.org/docs/usage.html



