Numbers_Pair = (2, 4, 6);
Fecha_Actual = (9, "Feb", 2024);

print(Numbers_Pair)
print(Fecha_Actual)

Amount_Words = int(input("¿Cuantas palabras va a agregar: "));

if (Amount_Words < 1):
    print ("Valor ingresado no valido. ");

else:
    
    List = [];
    
    for Index in range (Amount_Words):
        Word = input(f"Escriba la palabra que deseas almacenar {(Index + 1)}: ");
        List = List + [Word];
        
    print (f"La lista que se creo es: {List}");
    
List.append("Carlota");
List.remove(List[1]);

print (f"La lista que se creo es: {List}");
