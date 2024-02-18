Laboratory = int (0);

def Ejercicio_2():

    import random;
    global Laboratory;


    if Laboratory == 1:
            print("\n");
            Dado_Barbara = int (0);
            Dado_Alvaro = int (0);

            #Acá inicio el ejercicio #1:
            #Deben existir 2 dados el de Álbaro y el de Bárbara
            while Dado_Alvaro == Dado_Barbara:
                
                print("\n");
                print("------------------------------------------------------------");
                input("| Lanzando dado de Bárbara, presiona enter para continuar: |");
                Dado_Barbara = random.randint(1,6)
                
                print("\n");
                print("-----------------------------------------------------------");
                input("| Lanzando dado de Álvaro, presiona enter para continuar: |");
                Dado_Alvaro = random.randint(1,6)
                print("\n");

                if Dado_Alvaro > Dado_Barbara:
                    print(f"Álvaro es el ganador. Ya que saco {Dado_Alvaro} y Bárbara sacó {Dado_Barbara}");
                    print("\n");
                    break
                elif Dado_Barbara > Dado_Alvaro:
                    print(f"Bárbara es la ganadora. Ya que saco {Dado_Barbara} y Álvaro sacó {Dado_Alvaro}");
                    print("\n");
                    break
                else:
                    print(f"Ninguno ganó, fue un claro EMPATE, Bárbara sacó {Dado_Barbara} y Álvaro sacó {Dado_Alvaro}. ");
                    print("Volvamos a jugar. ");   
                    print("\n");    

def Ejercicio_3():

    print("\n");
    Num_Estudiantes = int(input("Ingrese la cantidad de estudiantes a dividir en los grupos: "));
    Grupo_A = 0;
    Grupo_B = 0;
    Sexo_System = "";

    for Names_Estudents in range (1, (Num_Estudiantes + 1)):
        Name = input(f"Ingrese el nombre del estudiante #{Names_Estudents} aquí: ");
        Name_System = Name.capitalize();
        Sexo = input("Por favor, ingrese 'M' si el Mujer y 'H' si es Hombre. ");
        Sexo_System = Sexo.upper();

        while ((Sexo_System != "M") and (Sexo_System != "H")):
            Sexo = input("Por favor, ingrese 'M' si el Mujer y 'H' si es Hombre. ");
            Sexo_System = Sexo.upper();

        if (Sexo_System == "M" and Name_System < "M") or (Sexo_System == "H" and Name_System > "N"):

            Grupo_A = Grupo_A + 1;
            print("Perteneces al grupo A. ");

        else:
            Grupo_B = Grupo_B + 1;
            print("Perteneces al grupo B. ");
        
    print(f"En el grupo A existen {Grupo_A} participantes.\nEn el grupo B existen {Grupo_B} participantes. "); 

def Ejercicio_4():

    #Acá inicio el ejercicio #3:
    #Maquinitas Precios: -4 años= Gratis / 4-18 años = 30000 / +18 años 50000
    Edad_Player = int (input ("Introduzca aquí su edad en años, por favor: "));

    if (Edad_Player < 4):
        print("\n");
        print("WoW, como tienes menos de 4 años no tienes que pagar tu boleta. ");
    elif (Edad_Player >= 4 and Edad_Player <= 18):
        print("\n");
        print("El costo a pagar es de: 30.000 $. ");
    else:
        print("\n");
        print("El costo a pagar es de: 50.000 $. ");  

def Ejercicio_5():

    Contraseña = "Contraseña"; 
    User_Password = "";

    print("\n","LOGIN","\n");

    while User_Password != Contraseña:
        User_Password = input("Por favor, ingrese su contraseña aquí: ");
        print("Contraseña incorrecta, por favor, ingresela nuevamente.");
        if User_Password == Contraseña:
            print("\n");
            print("CONTRASEÑA CORRECTA", "\n", "Bienvenido al sistema. ");

def Ejercicio_6():

    #Acá inicio el ejercicio #5:
    #Calcular el iva de un producto según lo que ponga el user, si no pone nada el IVA es del 21%

    print("\n    Calculadora de IVA", "\n");
    Produc_Price = float (input("Por favor, acontinuación ingrese el valor del producto: "))
    IVA = (input("Por favor ingrese el procentaje de IVA que se requiere: "))

    if IVA == '':
        try: 
            Iva_User = int(IVA);
        except ValueError:
            IVA = 0.21;
        
        IVA = Produc_Price * IVA;
        Produc_Price = Produc_Price + IVA;
        print("\n");
        print(f"El precio a pagar con IVA incluido es de: {Produc_Price}. ");

    else:
        IVA = float (IVA);
        IVA = (Produc_Price * IVA)/100;
        Produc_Price = Produc_Price + IVA;
        print("\n");
        print(f"El precio a pagar con IVA incluido es de: {Produc_Price}. "); 


def Ejercicio_7():

    Lista = [];

    Get_Out = 0;
    Number_User = 0;
    Contador_Numero = 0;
    Add_Number_List = 0;
    Index_List = 0;
    
    print("1. Añadir número a la lista. ");
    print("2. Añadir número a la lista en una posición. ");
    print("3. Longitud de la lista. ");
    print("4. Eliminar el último número de la lista. ");
    print("5. Eliminar un número según la posición. ");
    print("6. Contar un número. ");
    print("7. Posición(es) de un número. ");
    print("8. Mostrar todos los números. ");
    print("9. Salir. ");1

    Get_Out = int(input("--> "));



    while Get_Out != 9:

        if Get_Out == 1:

            print("Ingresa el número a almacenar en la lista: ");
            Add_Number_List = float(input("--> "));
            
            Lista.append(Add_Number_List);   
            
            input("Presiona espacio para continuar. ")

        elif Get_Out == 2:
    
            print("Ingresa el número a almacenar en la lista: ");
            Add_Number_List = float(input("--> "));

            print("Ingresa la posición en la que quieres guardar el elemento: ");
            print("Nota: La posición debe ser mayor a 0. ");
            Index_List = int(input("--> "));

            while Index_List <= 0:

                print("Valor ingresado no valido, intente nuevamente. ");
                print("\nIngresa la posición en la que quieres guardar el elemento: ");
                print("Nota: La posición debe ser mayor a 0. ");
                Index_List = int(input("--> "));            

            if len(Lista) < (Index_List - 1):

                print("La posición en la que desear agregar el número es más grande que el tamaño de la lista por lo cual se agregara de últimas. ");

            Lista.insert((Index_List - 1), Add_Number_List);

            input("Presiona espacio para continuar. ")

        elif Get_Out == 3:
            
            print("La longitud de la lista es de: ", len(Lista));

            input("Presiona espacio para continuar. ")

        elif Get_Out == 4:

            if len(Lista) == 0:
                
                print("La lista ya esta vacia por lo cual no se eliminara nada. ");

            else:    
                
                Lista.pop(-1);

            input("Presiona espacio para continuar. ")

        elif Get_Out == 5: 

            print("\nIngresa la posición del elemento que quieres eliminar: ");
            print("Nota: La posición debe ser mayor a 0. ");
            Index_List = int(input("--> "));   

            if Index_List >  len(Lista):

                print("El valor ingresado es mayor a la longitud de la lista por lo cuál no se puede eliminar algún valor. ");

            elif Index_List <= len(Lista):

                while Index_List <= 0:

                    print("Valor ingresado no valido, intente nuevamente. ");
                    print("\nIngresa la posición en la el elemento: ");
                    print("Nota: La posición debe ser mayor a 0. ");
                    Index_List = int(input("--> "));        

                Lista.pop((Index_List - 1));
            
            else:

                print("Lista vacia. :/ ");
        
            input("Presiona espacio para continuar. ")

        elif Get_Out == 6:

            print("Escribe el número que deseas contar: ");
            Number_User = float(input("--> "));

            if Number_User in (Lista):

                for Index_Number in (Lista):

                    if Index_Number == Number_User:

                        Contador_Numero = Contador_Numero + 1;1
                
                print(f"La cantidad de veces que aparece el número {Number_User} es de: {Contador_Numero}");

            else:
                
                print("El número solicitado no existe en la lista. ");
        
            input("Presiona espacio para continuar. ")

        elif Get_Out == 7:

            print("Escribe el número del que deseas conocer las posiciones en la que se encuentra: ");
            Number_User = float(input("--> "));

            if Number_User in (Lista):

                print("Las posiciones en las que se encuentra el número son las siguientes: ");

                Position_Number = 0;

                for Value_Number in (Lista):

                    if Value_Number == Number_User:

                        print(f"Posición #{Position_Number + 1}");
            
                    Position_Number = Position_Number + 1;
            
            else:
                
                print("El número solicitado no existe en la lista. ");
        
            input("Presiona espacio para continuar. ")

        elif Get_Out == 8: 

            print(Lista);
            input("Presiona espacio para continuar. ")

        elif Get_Out > 8 and Get_Out < 1:

            print("Selección de menu no valida, intentelo de nuevo. ");

        print("\n1. Añadir número a la lista. ");
        print("2. Añadir número a la lista en una posición. ");
        print("3. Longitud de la lista. ");
        print("4. Eliminar el último número de la lista. ");
        print("5. Eliminar un número según la posición. ");
        print("6. Contar un número. ");
        print("7. Posición(es) de un número. ");
        print("8. Mostrar todos los números. ");
        print("9. Salir. ");1

        Get_Out = int(input("--> "));


def Ejercicio_8():

    Stock_Of_Fruits = {};
    Number_Of_Fruits = 0;
    Want_To_Continue_User = 1;
    Want_To_Check_Total = 1;

    while Want_To_Continue_User == 1:

        print("\nPor favor, ingrese el nombre de la fruta a almacenar: ");
        Name_Fruit = input("--> ");

        print("Por favor, ingrese el precio de la fruta: ");
        Price_Fruit = input("--> ");
            
        Stock_Of_Fruits[Name_Fruit] = Price_Fruit

        print("\nSi desea continuar agregando productos al stock presione 1 de lo contrario presione cualquier otro número: ");
        Want_To_Continue_User = int(input("--> "));

    #print(Stock_Of_Fruits); Si funciona el guardado de datos en el diccionario. 

    Want_To_Continue_User = 1;

    print("\nSi desea consutar el precio por la cantidad de una respectiva fruta ingrese 1 de los contrario para finalizar, presione cualquier otro número: ");
    Want_To_Check_Total = int(input("--> "));

    if Want_To_Check_Total == 1:

        while Want_To_Continue_User == 1:

            print("\nPor favor, ingrese el nombre de la fruta que se va a comprar: ");
            Name_Fruit = input("--> ");

            print("Por favor, ingrese la cantidad de la fruta a comprar: ");
            Number_Of_Fruits = int(input("--> "));

            Total_Price = int(Stock_Of_Fruits[Name_Fruit]) * Number_Of_Fruits;

            print(f"Total de la compra de {Number_Of_Fruits} {Name_Fruit} es de: {Total_Price}");

            print("\nSi desea continuar consultando el total de compra de los productos presione 1 de lo contrario presione cualquier otro número: ");
            Want_To_Continue_User = int(input("--> "));

        print("\nThanks.  :D");


def Ejercicio_9 ():

    Carrito_De_Compras = {};
    Nombre_Articulo = "";
    Precio_Articulo = 0;
    Total_Precio = 0;
    Continue = 1;

    print("Ingrese 1 si desea agregar productos a su carrito de compra: ");
    Continue = int(input("--> "));

    while Continue == 1:

        print("Ingrese a continuacion el nombre del articulo a comprar: ");
        Nombre_Articulo = input("--> ");

        print("Ingrese a continuacion el precio del articulo a comprar: ");
        Precio_Articulo = float(input("--> "));

        Carrito_De_Compras[Nombre_Articulo] = Precio_Articulo;
        print("\n------------------------------------------------------------------------- ")
        print("Ingrese 1 si desea seguir agregando productos a su carrito de compra: ");
        Continue = int(input("--> "));
        print("\n------------------------------------------------------------------------- ")
        print("");



    for Index_Value in (Carrito_De_Compras.values()):

        Total_Precio = Total_Precio + Index_Value;

    print("Lista de la compra");
    print("   Articulo              Precio   ");

    for key, value in Carrito_De_Compras.items():

        print(key, "               " ,value);
        
    print("Total:               ", Total_Precio);

def Ejercicio_10():

    Grade_Student = 0;
    Amount_Students = 0;
    Number_Of_Grades = 0;
    Max_Amount_Of_Grades = 0;
    Grade_Students_List = [];
    Average = 0;
    Check_Average = 0;

    Grades_Students_Regist = {};
    Average_Grade_Students = {};

    print("Ingrese a continuación la cantidad de estudiantes que va a guardar: ");
    Amount_Students = int(input("--> "));

    for Index_Students_Names in range (Amount_Students):

        if Number_Of_Grades > Max_Amount_Of_Grades:

            Max_Amount_Of_Grades = Number_Of_Grades;

        Number_Of_Grades = 0;

        print(f"A continuacion, ingrese el nombre del estudiante #{Index_Students_Names + 1}: ");
        Student_Name = input("--> ");    

        while Student_Name in Grades_Students_Regist:

            print("El nombre ingresado ya existe. ");
            print(f"A continuacion, ingrese el nombre del estudiante #{Index_Students_Names + 1}: ");
            Student_Name = input("--> ");   

        print(f"Ingrese la nota #{Number_Of_Grades + 1} del estudiante: ");
        Grade_Student = float(input("--> "));

        Grade_Students_List = [];

        while Grade_Student > 0:

            Number_Of_Grades = Number_Of_Grades + 1;
            Grade_Students_List.append(Grade_Student);
            print(f"Ingrese la nota #{Number_Of_Grades + 1} del estudiante: ");
            Grade_Student = float(input("--> "));

        Grades_Students_Regist[Student_Name] = Grade_Students_List


    print("Si desea conocer el promedio de algun estudiante ingrese a continuación el #1 de lo contrario ingrese cualquier otro número para finalizar: ");
    Check_Average = int(input("--> "));

    while Check_Average == 1:

        print("Ingresa el nombre del estudiante del que se desea saber el promedio: ");
        Student_Name = input("--> ")

        if Student_Name in Grades_Students_Regist:

            for key, value in Grades_Students_Regist.items():
                Average = 0;
                for Index_Values in value:
                    Average = Average + Index_Values;
                Average = Average / Max_Amount_Of_Grades;
                Average_Grade_Students[key] = Average;

            print(f"El promedio de {Student_Name} es de: {Average_Grade_Students[Student_Name]}")

        else: 
            print("valor ingresado no valido. ");



print("Buenas tardes, soy Laboratory, a continuación te mostare las opciones que te puedo ofrecer: ","\n", "Escribe solo el número según corresponda a tu elección:", "\n", "1. Juego de Álvaro y Bárbara (Cada uno tira un dado)", "\n", "2. Grupos A y B ", "\n", "3. Pago de Boleta para entrar ", "\n", "4. Almacenamiento de contraseña ", "\n", "5. Calculadora de productos con IVA", "\n", "6. Para entrar al menu de una lista", "\n", "7. Para ingresar al registro de frutas", "\n", "8. Para entrar en una lista de compras", "\n", "9. Para ingresar al registro de notas y nombres de alumnos", "\n", "10. Para finalizar el programa");
Laboratory = int(input("Ingresa a continuación el número del programa a utilizar: "));


while Laboratory != 10:

    if Laboratory == 1:

        Ejercicio_2();

    elif Laboratory == 2:

        Ejercicio_3();

    elif Laboratory == 3:

        Ejercicio_4();

    elif Laboratory == 4:

        Ejercicio_5();

    elif Laboratory == 5:

        Ejercicio_6();

    elif Laboratory == 6:

        Ejercicio_7();

    elif Laboratory == 7:

        Ejercicio_8();

    elif Laboratory == 8:

        Ejercicio_9();

    elif Laboratory == 9:

        Ejercicio_10();

    print("\nBuenas tardes, soy Laboratory, a continuación te mostare las opciones que te puedo ofrecer: ","\n", "Escribe solo el número según corresponda a tu elección:", "\n", "1. Juego de Álvaro y Bárbara (Cada uno tira un dado)", "\n", "2. Grupos A y B ", "\n", "3. Pago de Boleta para entrar ", "\n", "4. Almacenamiento de contraseña ", "\n", "5. Calculadora de productos con IVA", "\n", "6. Para entrar al menu de una lista", "\n", "7. Para ingresar al registro de frutas", "\n", "8. Para entrar en una lista de compras", "\n", "9. Para ingresar al registro de notas y nombres de alumnos", "\n", "10. Para finalizar el programa");
    Laboratory = int(input("Ingresa a continuación el número del programa a utilizar: "));