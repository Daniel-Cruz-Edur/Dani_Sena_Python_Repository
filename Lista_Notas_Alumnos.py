""" 
Nombre de los alumnos. 4 alumnos. 
Notas de los alumnos. 0-4 Malo 5-7 Bueno 8-10 Sobresaliente.
"""
Amount_Students = 4;
Names = [];
Grades = [];
Great_Grade_Counter = 0;
Normal_Grade_Counter = 0;
Bad_Grade_Counter = 0;

for Index in range (Amount_Students):
    Name_Student = input(f"Por favor ingrese el nombre del alumno # {(Index + 1)}: ");
    Names.append(Name_Student);
    Grade_Student = int(input("Por favor ingrese la nota del alumno: "));
    Grades.append(Grade_Student);
    
""" 

for Index in range (Amount_Students):

    print("\n")
    print(Names[Index]);
    print(Grades[Index]);

    if Grades[Index] >= 8:
        print("Alumno muy bueno. ");
        Great_Grade_Counter = Great_Grade_Counter + 1;
        
    elif Grades[Index] >= 4:
        print("Alumno bueno. ");
        Normal_Grade_Counter = Normal_Grade_Counter + 1;
        
    else: 
        print("Alumno no aprueba. ")
        Bad_Grade_Counter = Bad_Grade_Counter + 1;  

print(end='\n');
print("La cantidad de alumnos muy buenos son: ", Great_Grade_Counter);
print("Los nombres de los alumnos muy buenos son: ");

for Index in range (Amount_Students):
    
    if Grades[Index] >= 8:
        
        print("\n");
        print("Estudiante #", (Index + 1), Names[Index]);
        print("La nota del estudiante es: ", Grades[Index]);

"""
for Index in range (len(Grades)):    

    if Grades[Index] >= 4 and Grades[Index] <= 7:
        
        Grades.pop(Index);
        Names.pop(Index);
        print("\n");
        #print("Estudiante #", (Index + 1), Names[Index]);
        #print("La nota del estudiante es: ", Grades[Index]);

print("Listado de alumno con notas entre 4-7: ", Names, Grades);
