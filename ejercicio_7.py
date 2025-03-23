num = int(input("Ingrese un número al cuál quiere generar la secuencia: "))

string_consola = ""

#Generador de la secuencia, los pares se vuelven negativos y los impares quedan positivos
for n in range(num):
    if (n+1)%2 == 0:
        string_consola += f"{str((n+1)*-1)} "
    else:
        string_consola += f"{str(n+1) } "

print(f"la secuencia es : {string_consola}")
