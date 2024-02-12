Integrer_Numbers = [];
Amount_Numbers = 5;
    
def Login():
    
    for Index in range (Amount_Numbers):
        Number = int(input("Por favor, ingresa el número a almacenar: "));
        Integrer_Numbers.append(Number);
        
def Print(Integrer):
    print("Los datos de la lista son: ")
    
    for Index in range (Amount_Numbers):
        print(Integrer_Numbers[Index]);
        
def Sum(List_Numbers):
    
    Numbers_Sum = 0;
    
    for Index in range (Amount_Numbers):
        Numbers_Sum = Numbers_Sum + Integrer_Numbers[Index];
    
    
        
Login();
Print(Integrer_Numbers);