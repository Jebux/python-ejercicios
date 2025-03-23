#importación de la libreria math
import math

#ingreso de cada una de las variables
print("Ingrese las coordenadas de los puntos que quiere conocer la distancia entre ellos")
x1 = math.radians(float(input("Ingrese el x1: ")))
y1 = math.radians(float(input("Ingrese el y1: ")))
x2 = math.radians(float(input("Ingrese el x2: ")))
y2 = math.radians(float(input("Ingrese el y2: ")))

radio_tierra=6371

#Calculo de la distancia
def calculo_distancia():
    distancia = radio_tierra*math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
    return distancia

print(f"La distancia es {calculo_distancia():.2f} km")