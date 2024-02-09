import datetime;

"""

Date_User = int(input("Por favor ingrese el año en que esta cursando actualmente: "));
Is_Year_Leap = int(input("Por favor, ingrese un año para decirle si es bisiesto o no. "));

def Leap_Year_User_Year(Year):
    
    print("Tu fecha actal es: ", Date_User);
    
    if ((Year % 4 == 0) and (Year % 100 != 0)):
        print("El año cursado es un año bisiesto. ");
    
    elif ((Year % 100 == 0) and (Year %400 == 0)):
        print("El año cursado es un año bisiesto. ");
        
    else:
        print("El año cursado NO es un año bisiesto. ");

def To_Known_Is_A_Year_Leap(Is_A_Leap_Year):
    
    print("La fecha proporcionada es: ", Is_Year_Leap);
    
    if ((Is_A_Leap_Year % 4 == 0) and (Is_A_Leap_Year % 100 != 0)):
        print("El año proporcionado es un año bisiesto. ");
    
    elif ((Is_A_Leap_Year % 100 == 0) and (Is_A_Leap_Year %400 == 0)):
        print("El año proporcionado es un año bisiesto. ");
        
    else:
        print("El año proporcionado NO es un año bisiesto. ");

"""

Year_To = int(input("Por favor ingrese la fecha desde la que desea saber si es año bisiesto (La fecha Menor): "));
Year_Until = int(input("Por favor ingrese la fecha hasta la cual desea saber si es año bisiesto (La fecha Mayor): "));

def To_Year_Until_Year_How_Many_Leap(Initial_Year):
    
    Amount_Years = Year_Until - Year_To;
    Leap_Years_Counter = 0;
    Not_Leap_Years_Counter = 0;
    
    for Index in range (Amount_Years):
        
        if ((Initial_Year % 4 == 0) and (Initial_Year % 100 != 0)):
            Leap_Years_Counter = Leap_Years_Counter + 1;

        elif ((Initial_Year % 100 == 0) and (Initial_Year %400 == 0)):
            Leap_Years_Counter = Leap_Years_Counter + 1;
            
        else:
            Not_Leap_Years_Counter = Not_Leap_Years_Counter + 1;

        Initial_Year = Initial_Year + 1;

    print("La cantidad de años bisiestos en ese rango de tiempo es de: ", Leap_Years_Counter);
    print("La cantidad de años no bisiestos es de: ", Not_Leap_Years_Counter);

To_Year_Until_Year_How_Many_Leap(Year_To);
#Leap_Year_User_Year(Date_User);
#To_Known_Is_A_Year_Leap(Is_Year_Leap);

