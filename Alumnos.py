""" 
Codifica un programa en python que nos permita guardar los nombres de los 
alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
distinta cantidad de notas. Guarda la información en un diccionario cuya 
claves serán los nombres de los alumnos y los valores serán listas con las 
notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su
nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.

al final nos debe mostrar la
la lista de los alumnos con el promedio de cada uno , si al ingresar un nombre que ya existe debe salir debe salir un mensaje de que ya existe

"""
Amount_Students = 0;

print("Ingrese a continuación la cantidad de estudiantes que va a guardar: ");
Amount_Students = int(input("--> "));

for Index_Students_Names in range (Amount_Students):
    
    print();