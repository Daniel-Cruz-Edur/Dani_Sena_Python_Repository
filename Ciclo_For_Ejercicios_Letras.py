Frase = input("Por favor ingrese una frase: ");
Letra = input("Por favor ingrese la letra a buscar: ");
Contador_Letra = 0;

for Index in (Frase):
    if Index == Letra:
        Contador_Letra = Contador_Letra + 1;
        print("Pase por aqui. ");

print("La cantidad de veces que aparece la letra '", Letra ,"' es de: ", Contador_Letra, "veces.");

print("-----------------------------------------------\n\n\n");
for X in range (1, 21, 2):
    print(X);
