import datetime
#from tabulate import tabulate 
global datos 
global encabezado
datos= []  
encabezado=[]

def registrar():
    fechaInicio=input("Fecha de inicio de registo (d/m/y):")
    fechaFin=input("Fecha fin de registo (d/m/y):")
    pacientes=input("Cantidad de pacientes:")
    
    date1 = datetime.datetime.strptime(fechaInicio,"%d/%m/%y")
    date2 = datetime.datetime.strptime(fechaFin,"%d/%m/%y")
    dif= (date2-date1).days
    
    encabezado=[]
    for i in range (0, dif):
        fecha=fecha + datetime.timedelta(days=1)
        encabezado.append(fecha.strftime("%d/%m/%y"))
        print (encabezado)
        
    for i in range (0, pacientes+1):
        fila=["P"+str(i+1)]
        for j in range (0, dif+1):
            fila.append(0)
            datos.append(fila)
            print (tabulate(datos, encabezado, tablafmt="grid"))
            
def estadisticas():
    pass

def menu():
    print("Bienvendio al sistema")
    print("1. Registrar datos")
    print("2. Estadisticas")
    opcion=input("Seleccione:")
    
    if opcion=="1":
        registrar()
    elif opcion=="2":
        estadisticas()
    else:
        print("opcion invalida")
        menu()

menu()
