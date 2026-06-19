
#Declaramos una variable
#el metodo open me busca o crea un archivo
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')#w = write = escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos som importantes para las palabras.\n')
    archivo.write('como por ejemplo:acción, ejecución y producción.\n')
    archivo.write('las letras son: \nr read leer, \na append anexa, \nw write escribir, \nx crea un archivo')
    archivo.write('\nt es para texto o text, \nb es para archivo binarios, \nw+ escribe y lee informacion son iguales r+\n')
    archivo.write('Saludos a todos los alumnnos de la tecnicatura')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)#en caso de algun error muestra cual es
finally:#siempre se ejecuta
    archivo.close()#con esto se cierra el archivo

#archivo.write('Todo quedo perfecto')me marca error porque anteriormente cerre el archivo


