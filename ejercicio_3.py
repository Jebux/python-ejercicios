"""
Escribe una función que dados 3 números, determine si los números se están
incrementando, disminuyendo o ninguno de lo anterior.

Por ejemplo: 1, 4, 19 --> están incrementando; 33, 10 ,1 --> están disminuyendo;
3 , 18 , 10 --> Ni se incrementa ni se disminuye.
"""
#Lista que va a almacenar los datos ingresados por el usuario
numeros = []

print("Acontinuación ingrese 3 números para ser analizados.")

#Mientras el usuario no ingrese los 3 datos le va a solicitar que los ingrese y cada vez que los ingrese los agrega al listado.
while (len(numeros) < 3):
    num = int(input("Ingrese un número:"))
    numeros.append(num)

#variables para identificar los incrementos o decrementos
aumento = 0
disminuye = 0

#Recorrer el listado para compararlos. Se utiliza enumerate para hacer uso de él dentro del for. 
for i, num in enumerate(numeros):
    #En la primera ronda salta las otras comparaciones
    if i == 0:
        continue
    #Después de la primera ronda compara el número actual con el anterior y dependiendo si es mayor o menor, aumenta los acumuladores de disminuye o de aumento
    if num > numeros[i-1]:
        aumento+=1
    if num < numeros[i-1]:
        disminuye+=1

#Variable para preparar el mensaje de consola con el formato de "num1, num3, num4"
listado_string = ""
#Recorre el listado de números
for num in numeros:
    listado_string = listado_string + str(num) 
    #Si no es el último agregue un ", " al final del string
    if num != numeros[len(numeros)-1]:
        listado_string += ", "

#Condicionales a partir de los acumuladores para saber si está incrementando, disminuyendo o ninguna de los dos.
if disminuye == 0:
    print(f"{listado_string} -> están incrementando")
elif aumento == 0:
    print(f"{listado_string} -> están disminuyendo")
else: 
    print("Ni se incrementa ni se disminuye")