num = int(input("Ingrese el número de filas: "))

num_string = ""
filas =1

print("""
La secuencia es:
""")
#A partir del valor dado empieza a iterar agregando cada valor de las iteraciones al string que se imprime
for n in range(num):
    num_string += str(filas)
    filas += 1
    print(num_string)
