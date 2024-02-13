def Registrar():
    Agenda={
        
    };
    Answer = "S";
    while Answer == "S":
        
        Date = input("Ingrese la fecha con formato DD/MM/AA: ");
        List_Dates = []
        
        while Answer == "S":
            
            Hour = input("Ingresar la hora de la actividad Horas/Minutos: ");
            Activity_Name = input("Ingrese el nombre de la actividad: ");
            List_Dates.append((Hour, Activity_Name));
            Answer = input("¿Desea agregar otra actividad para la misma fecha?  S/N: ");
        
        Agenda[Date]= List_Dates;
        
        Answer = input("¿Desea agregar otra fecha?  S/N: ");

    return Agenda;

def Mostrar(Agenda):
    
    print("Listado de la agenda: ")
    for Date in Agenda:
        print("Para la fecha: ", Date);
        for Hour, Activity_Name in Agenda[Date]:
            print(Hour, Activity_Name);
         
def Consultar_Fecha():
    
    Date = input("Ingrese la fecha que desea consultar: ");

    if Date in Agenda:
        
        for Hour, Activity_Name in Agenda[Date]:
            print(Hour, Activity_Name)
    
    else: 
        print("No existe ninguna actividad guardada en esa fecha");

Agenda = Registrar();
Mostrar(Agenda);
Consultar_Fecha();