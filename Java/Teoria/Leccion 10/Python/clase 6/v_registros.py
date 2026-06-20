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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los id_persona a buscar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(', ')),)#es una sola tupla colocar coma
            #Si le agrego mas registros y estos no existen, no los muestra por consola
            #id_persona = input('Digite un numeropara el id_persona: ')
            cursor.execute(sentencia, llaves_primarias)#de esta manera ejecutamos la sentencia
            registros = cursor.fetchall()#recupera todos los registros que seran una lista
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()