"""Datos que se ingresan
|     Bulto    |   Peso (kg)  |
______________________________
        0            502    -----> Dato erroneo
        1            35
        2            23
        3            78
        4            500
        5            197
        6            450 
        7            150
        8            98
        9            99
        10           134
        11           50
        12           27
        13           7 
        14           15
        15           21
______________________________

"""

capacidad_Boeing747 = 18000
#booleanos para saber si se ingresa los datos uno a uno o decide usar la lista predefinida
ingresar_datos = True
new_paquete = True


peso_paquete = 0
bultos_pre = [35,23,78,500,197,450,150,98,99,134,50,27,7,15,21]
bultos = []

# Mensaje si el usuairo quiere ingresar los datos manualmente o quiere usar la lista predefinida
while(True):
    message_first = input("¿Quiere ingresar de cero los número? (s/n): ")
    if message_first == "n":
        bultos = bultos_pre
        ingresar_datos = False
    if message_first == "s" or message_first == "n":
        break

#Ingreso de datos para la lista manual
if ingresar_datos:
    while(new_paquete):
        peso_paquete = int(input("Ingrese el peso del paquete "))
        if peso_paquete>500 or peso_paquete<0:
            print("El paquete no puede subir")
            continue
        bultos.append(peso_paquete)
        #mensaje para si quiere ingresar más bultos    
        while (True):
            message = input("¿Desea ingresar otro bulto? (s/n) ")
            if message == "n":
                new_paquete = False
            if message == "s" or message == "n":
                break

#promedio
def media():
    promedio = 0
    suma = 0
    for bulto in bultos:
        suma += bulto
        promedio  = suma/len(bultos)
    return promedio

#ingreso en moneda local/peso
def ingreso_peso():
    ingreso = 0
    for bulto in bultos:
        if bulto <= 25:
            continue
        elif bulto < 300:
            ingreso += 1500 * bulto
        else:
            ingreso += 2500 * bulto
    return ingreso

#conversión a dolares
def ingreso_dolares():
    return round(ingreso_peso()/4114, 2)

#mensaje final
print(f"""
El número de bultos es {len(bultos)} unidades
El bulto más pesado pesa: {max(bultos)} kg
El bulto más liviano pesa: {min(bultos)} kg
El promedio del peso de los bultos es: {media()} kg
El ingreso por la carga es: $ {ingreso_dolares()} USD

""")
