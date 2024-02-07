""" 
1). Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura 
    promedio de las personas.
2). En una empresa privada  trabajan en empleados de planta cuyos sueldos oscilan 
    entre $1300.000 y $10.000.000, El programa debe realizar lo siguiente:

    Leer los sueldos que cobra cada empleado e informe cuántos empleados cobran 
    entre $10.000.000 y $300.000  y cuántos cobran más de $3000.000. 
    Además el programa deberá informar el importe que gasta la empresa en sueldos 
    al personal.

"""



Height_Average = 0;
User_Height = 0;
Amount_Of_Persons = 0;

print("A continuación ingresa cuántas medidas vas a ingresar: ");
Amount_Of_Persons = int(input("--> "));

for Index in range (0, Amount_Of_Persons):
    print("Ingresa aquí las medidas de la persona #",(Index+1), ", recuerda ingresar los datos en metros(m): ");
    User_Height = float(input("--> "));
    Height_Average =  Height_Average + User_Height; 

Height_Average = Height_Average/Amount_Of_Persons;
print("La altura promedio del grupo de personas ingresado es de: ", "{0:.3f}".format(Height_Average));



Amount_Employee_Normal_Salary = 0;
Amount_Employee_More_3_Millon = 0;
Amount_Employee__Not_Normal_Salary = 0;
Employee_Salary = 0;
Amount_Of_Employee = 0;
Salary_Cost_To_The_Corp = 0;

print("A continuación ingresa la cantidad de empleados que vas a registrar: ");
Amount_Of_Employee = int(input("--> "));


for Index in range (0, Amount_Of_Employee):
    print("Ingresa aquí el salario del empleado #",(Index+1), ", recuerda ingresar los datos en COP($): ");
    Employee_Salary = float(input("--> "));
    
    Salary_Cost_To_The_Corp = Salary_Cost_To_The_Corp + Employee_Salary;

    if Employee_Salary > 3000000:
        Amount_Employee_More_3_Millon = Amount_Employee_More_3_Millon + 1;
    
    elif Employee_Salary >= 1800000 and Employee_Salary < 3000000:      
        Amount_Employee_Normal_Salary = Amount_Employee_Normal_Salary + 1;
    
    else:
        Amount_Employee__Not_Normal_Salary = Amount_Employee__Not_Normal_Salary + 1;    

    
print("Actualmente en la empresa existen ", Amount_Employee_Normal_Salary, " personas cuyo salario se encuentra entre $1'800.000 y $3'000.000 COP. ");
print("De los empleados registrados ", Amount_Employee_More_3_Millon, " tienen un salario de 3'000.000 o superior. ") 
print("El número de empleados con un salario menor a 1'800.000 es de: ", Amount_Employee__Not_Normal_Salary, "Empleados");   
print("Y el costo total de importe de la empresa por el pago de los salarios es de: ", Salary_Cost_To_The_Corp);   
    
    
    
""" Se cuenta con la siguiente información:
Las edades de 6 estudiantes del turno mañana.
Las edades de 7 estudiantes del turno tarde.
Las edades de 12 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los 
tres turnos tiene un promedio de edades mayor."""


Age_Student = 0;
Numbers_Students_Morning = 6;
Numbers_Students_Afternoon = 7;
Numbers_Students_Evening = 12;
Average_Age = 0;
Average_Age_Morning = 0;
Average_Age_Afternoon = 0;
Average_Age_Evening = 0;
Biggest_Average_Age = 0;

print("Primero registra los estudiantes del horario de la mañana: \n");

for Students_Morning in (0, Numbers_Students_Morning):
    print("A continuación ingresa la edad del estudiante #", (Students_Morning + 1), "del horario de la mañana: \nNota: La edad debe ser ingresada en años. ");
    Age_Student = input("-->");
    Average_Age_Morning = Average_Age + Age_Student;
    
print("Ahora registra los estudiantes del horario de la tarde: \n");

for Students_Afternoon in (0, Numbers_Students_Afternoon):
    print("A continuación ingresa la edad del estudiante #", (Students_Afternoon + 1), "del horario de la tarde: \nNota: La edad debe ser ingresada en años. ");
    Age_Student = input("-->");
    Average_Age_Afternoon = Average_Age + Age_Student;
    
print("Por último registra los estudiantes del horario de la noche: \n");
    
for Students_Evening in (0, Numbers_Students_Evening):
    print("A continuación ingresa la edad del estudiante #", (Students_Evening + 1), "del horario de la noche: \nNota: La edad debe ser ingresada en años. ");
    Age_Student = input("-->");
    Average_Age_Evening = Average_Age + Age_Student;
    
if (Average_Age_Morning > Biggest_Average_Age):
    Biggest_Average_Age = Average_Age_Morning;
    
    if (Average_Age_Afternoon > Biggest_Average_Age):
        Biggest_Average_Age = Average_Age_Afternoon; 
    
    elif (Average_Age_Evening == Biggest_Average_Age):
        
        print("El promedio más grande de edades es el de el grupo del horario de la Tarde y el grupo de la noche.\nCon un promedio de: ", Average_Age_Afternoon, "años. ");
        
        if (Average_Age_Evening > Biggest_Average_Age):
            print("El promedio más grande de edades es el de el grupo del horario de la noche.\nCon un promedio de: ", Average_Age_Evening, "años. ");
            
    elif (Biggest_Average_Age > Average_Age_Evening):
        print("El promedio más grande de edades es el de el grupo del horario de la mañana.\nCon un promedio de: ", Average_Age_Morning, "años. ");
            
        if (Biggest_Average_Age == Average_Age_Evening):
            print("El promedio más grande de edades es el de el grupo del horario de la mañana y el grupo de la noche.\nCon un promedio de: ", Average_Age_Morning, "años. ");


