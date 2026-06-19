#r = read
#w = write
#a = append = anexa un archivo
#x = crea un archivo y devuelve erro si no encuentra el texto
#archivo = open('prueba.txt', 'a')

archivo = open('prueba.txt', 'r', encoding= 'utf-8' )
#print(archivo.read())
#print(archivo.read(15))#me permite leer cantidad de caractares
#print(archivo.read(5))#continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

#vamos a iterar cada una de las lineas
#for linea in archivo:
    #print(linea)
#print(archivo.readlines()[3])# acccedemos al archivo como si fuera una lista
#Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding= 'utf-8')
archivo2.write(archivo.read())
archivo.close()#cerramos el primer archivo
archivo2.close()#cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
#se vuelvo a ejecutar no se genera otro archivo de copia, pero si dentro de el se repite

