""" 
De una empresa de transporte se quiere guardar el nombre de los 
conductores que tiene, y los kilómetros que conducen cada día de la semana.

Para guardar esta informacion
Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales 
que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conductores y los 
kilómetros que ha realizado.

"""
Amount_Drivers = 0;
Names_Drives_List = [];
Km__Driver_List = [];
Week_Days = 7;
Collector_Km = 0;

print("Ingrese la cantidad de camioneros que va a registrar: ");
Amount_Drivers = int(input("--> "));

for Index in range (Amount_Drivers):
    
    print(f"A continuación ingrese el nombre del conductor #{Index + 1} que va a registrar: ");
    Driver_Name = input("--> ");
    Names_Drives_List.append(Driver_Name);
    
for Index_Driver in range (Amount_Drivers):    
    
    Collector_Km = 0;
    
    for Index_Km in range (Week_Days):
        print("\nDías de la semana: ");
        print("1 = Lunes\n2 = Martes\n3 = Miercoles\n4 = Jueves\n5 = Viernes\n6 = Sabado\n7 = Domingo");
        print(f"\nA continuación ingrese el total de Km del conductor #{Index_Driver + 1} llamado {Names_Drives_List[Index_Driver]}. Del cual va a registrar los KM  del día #{Index_Km + 1}: ");
        Collector_Km = Collector_Km + float(input("--> "));
    
    Km__Driver_List.append(Collector_Km);
    
print("Los nombres de los conductores registrados son los siguiente y sus respectivos km totales: ")
print(Names_Drives_List, Km__Driver_List);
    

        
        
