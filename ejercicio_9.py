#Determinar los factores de un número.

num = int(input("¿Qué número desea analizar? "))

acumulador =0
for n in range(num):
    if n == 0:
        continue
    #Para que un número sea factor de otro, significa que su modulo es igual a cero
    if num % n == 0:
        print(f"El número {num} es divisible entre {n} ")
        acumulador += 1

print(f"El número {num} tiene {acumulador} factores")