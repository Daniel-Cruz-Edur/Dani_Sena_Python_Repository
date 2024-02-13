Persona = {
    "Nombre": "Daniel Eduardo",
    "Apellido": "Cruz Gonzalez",
    "Estatura": 1.59,
    "Edad": 18,
    "Email": "Danielmico02@gmail.com",
    "Pais de origen": "Colombia",
    "Ciudad de nacimiento": "Bogotá",
    "Genero": ["Femenino","Masculino", "Otre"]
}



print(Persona);
print(Persona["Nombre"]);
print(f"El nombre de la persona es: {Persona['Nombre']}");

#Así se agregan elementos a un diccionario
Persona["Telefono"]=333333333;
print(Persona);

#Modificar el valor del diccionario
Persona["Telefono"]=444444444;
print(Persona);

#Modificar la clave del elemento
Persona["Celular"]=Persona.pop("Telefono");
print(Persona);

#Eliminar un elemento del diccionario
del Persona["Celular"];
print(Persona); 

#Iterar los items de las claves y valores
for clave, valor in Persona.items():
    print(clave ,  ": " , valor);
    
