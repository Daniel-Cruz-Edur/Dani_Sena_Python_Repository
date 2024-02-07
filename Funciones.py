def Start():
    print("Menu Principal");
    print("Selecciones la opcion correcta: ");
    print("1. Para sumar. \n2. Para restar. \n3.Para multiplicar. \n4. Para dividir. \n5. Salir. ");

def Sum():
    Num_1 = int(input("Ingrese el primer número: "));
    Num_2 = int(input("Ingrese el segundo número: "));
    Suma = Num_1 + Num_2;
    print("El resultado de la suma es: ", Suma);
    
def Res():
    Num_1 = int(input("Ingrese el primer número: "));
    Num_2 = int(input("Ingrese el segundo número: "));
    Minus = Num_1 - Num_2;
    print("El resultado de la suma es: ", Minus); 

def Mul():
    Num_1 = int(input("Ingrese el primer número: "));
    Num_2 = int(input("Ingrese el segundo número: "));
    Multipli = Num_1 * Num_2;
    print("El resultado de la suma es: ", Multipli); 
    
def Div():
    Num_1 = int(input("Ingrese el primer número: "));
    Num_2 = int(input("Ingrese el segundo número: "));
    Multipli = Num_1 / Num_2;
    print("El resultado de la suma es: ", Multipli); 
    
def Exit():
    print("Hasta luego. Te espero en una siguiente ejecución de codigo. ");

def Main():
    while True:
        Start();
        Election = int(input("Selecione su opción: "));
        if Election == 1:
            Sum();
        elif Election == 2:
            Res();
            
        elif Election == 3:
            Mul();
            
        elif Election == 4:
            Div();
            
        elif Election == 5:
            Exit();
            
Main();