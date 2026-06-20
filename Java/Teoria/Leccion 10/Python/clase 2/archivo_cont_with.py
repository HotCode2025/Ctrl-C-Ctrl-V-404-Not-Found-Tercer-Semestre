
from Manejoarchivos import ManejoArchivos
#Manejo de contexto with: sintaxis simplificada
#with open('prueba.txt', 'r', encoding= 'utf-8') as archivo:
#   print(archivo.read())
#No hace falta el try ni el finally
#en el contexto de with se ejecuta de maner automatica
#Utiliza diferentes metodos: __enter__ abre el archivo
#Este metodo cierra: __exit__


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

