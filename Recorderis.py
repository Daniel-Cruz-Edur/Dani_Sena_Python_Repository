"""Preguntar la edad del usuario 
<4 años gratis
4-8 5000
>18 10000 """

Edad = int (input("Por favor, ingrese su edad: "));

if Edad < 4:
    Ingreso = 0;
    print("El costo de ingreso es de: ", Ingreso);
elif Edad <= 18:
    Ingreso = 5000; 
    print("El costo de ingreso es de: ", Ingreso);
else: 
    Ingreso = 10000;
    print("El costo de ingreso es de: ", Ingreso);