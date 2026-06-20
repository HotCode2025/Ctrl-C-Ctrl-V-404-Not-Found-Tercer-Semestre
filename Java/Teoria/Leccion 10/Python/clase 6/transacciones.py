import psycopg2 as bd#para conectarnos a posgresql

conexion = bd.connect(
    user= 'postgres',
    password= 'Admin',
    host= '127.0.0.1',
    port= '5432',
    database= 'test_bd'
)
try:
    #conexion.autocommit = False#me indica que yo debo guardar los cambio, no se va a realizar por defecto
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ("Maria", "Esparta", "mariesperta@gmail.com")
    cursor.execute(sentencia, valores)
    conexion.commit()#hacemos el commit manualmente
    print('Termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()