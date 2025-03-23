num_binario = input("Ingrese el número binario: ")

decimal = 0

#Revierte el número que ingresó el usuario
num_binario_rev = num_binario[::-1]

#Se recorre el número ingresado como una string y se apoya de la posición de cada uno de los números para la fórmula de cada número de derecha a izquierda es (digitoBinario * 2 ^ al index o posición)
for i,num in enumerate(num_binario_rev):
    decimal += (int(num)*(2**i))
    
print(f"El número binario {num_binario} es el número decimal {decimal}")