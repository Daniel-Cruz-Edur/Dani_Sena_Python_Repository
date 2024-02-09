Debe_Recibir_Un_Saludo = "Buenos días, ¿A su merced se le ofrece una arepita?.";

def Mensaje():
    
    Num_1 = int(input("Ingresa el primer número: "));
    Num_2 = int(input("Ingresa el segundo número: "));
    Calculo_Mayor(Num_1, Num_2);
    Positivo(Num_1, Num_2);
    
def Calculo_Mayor(Number_1, Number_2):
    
    if (Number_1 > Number_2):
        print("El primer número es mayor");
    elif (Number_2 > Number_1):
        print("El segundo número es mayor");
    else:
        print("Los 2 números son iguales. ");
        
def Positivo(Number_1, Number_2):
    
    if (Number_1 > 0):
        print("El primer número es positivo. ");
        Number_1 = True;
        
    elif (Number_1 == 0):
        print("El primer número es igual a 0; ");
    else:
        print("El primer número es negativo. ");
        Number_1 = False;
       
               
    if (Number_2 > 0):
        print("El segundo número positivo. ");
        Number_2 = True;
        
    elif (Number_2 == 0):
        print(" El segundo número es igual a 0; ");
        
        
    else:
        print("El segundo número es negativo. ");
        Number_2 = False;
    
    if (Number_1 and Number_2 == True):
        print("Los 2 números son positivos. ");
    
    elif (Number_1 and Number_2 == False):
        print("Los 2 números son negativos. ");
        
    elif (Number_1 and Number_2 == 0):
        print("Los 2 números son iguales a 0. ");


Mensaje();