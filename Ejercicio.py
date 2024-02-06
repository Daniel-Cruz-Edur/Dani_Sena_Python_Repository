Contador = 0;
Numeros = 0;
User_Number = 0;

while Contador < 10:
    User_Number = float(input("Ingresa el valor: "));
    Numeros += User_Number;
    Contador += 1;


Numeros = Numeros/10;
print("El promedio de los números es de: ", Numeros);
    