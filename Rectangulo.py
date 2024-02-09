Width = int(input("Ingrese el ancho del rectangulo (int): "));
Height = int(input("Ingrese la altura del rectangulo (int): "));
Simbol = input("Ingrese el caracter a utilizar: ");

def Dibujo(Long, Tall, Character):
    for Index in range (Long):
        print(Character);
        for Index_2 in range (Tall):
            print(Character);
            
Dibujo(Width, Height, Simbol);