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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los numeros de registro a eliminar: ')
            valores = (entrada, )
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount#
            print(f'Los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()