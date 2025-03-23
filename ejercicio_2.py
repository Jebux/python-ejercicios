# Escribe un algoritmo que determine el valor de un pasaje en avión, conociendo la distancia a recorrer, el número de días de estancia, y sabiendo que, si la distancia a recorrer es superior a 1000 Km y el número de días de estancia es superior a 7, la línea aérea le hace un descuento del 15%. (el precio por km. es de $5.000 aunque el mínimo a cobrar siempre es $100.000)

print("""
Inicializando programa para valor de pasaje de avión..
      """)

#Ingreso de la información del usuario sobre la distancia a recorrer y el número de estancia en el lugar.
distancia_recorrer = int(input("Ingrese la distancia que va a recorrer: "))
numero_estancia = int(input("Ingrese el número de días de estancia: "))

#Calculo del valor de "la gasolina" considerando que es 5000 por cada kilometro
valor_gasolina = 5000*distancia_recorrer
valor_pasaje = 0

#Si el valor de la gasolina es menor a 100k se cobra 100k
if(valor_gasolina<100000):
    valor_pasaje = 100000
#Si es mayor a 100k se cobra lo que indique la operación
else:
    valor_pasaje = valor_gasolina

#Si la distancia a recorrer es superior a 1000 y el número de estancia es mayor a 7 se aplica un 15% de descuento
if(distancia_recorrer>1000 and numero_estancia>7):
    valor_pasaje = valor_pasaje*0.85

#Impresión del valor del pasaje
print(f"El valor del pasaje es: ${valor_pasaje}")