import random

Secreto = random.randint(1, 10);
    
Num_User = int(input("Ingresa un número entre 1 y 10: "));


while Num_User != Secreto:

    if Num_User < Secreto:
        print("El número secreto es mayor.");
        print("Intenta nuevamente. ");

    elif Num_User > Secreto:
        print("El número secreto es menor.");
        print("Intenta nuevamente. ");
        
    Num_User = int(input("Ingresa un número entre 1 y 10: "));

input("Felicdades, haz adivinado el número secreto. ");



    