list_hex_letras = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
#list_decimal =    [0,1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15]

num_dec = int(input("Ingrese un número decimal para convertir a hexagesimal: "))

num_dec2 = num_dec

def convertidor_hex(num_dec):
    num_hex = ""
    #Divide el valor ingresado en 16, el cociente se sigue dividiendo hasta  que llegue a cero y el residuo se usa para buscarlo en el listado
    while num_dec>0:
        cociente = int(num_dec/16)
        residuo = num_dec%16
        num_hex += str(list_hex_letras[residuo])
        num_dec = cociente
    #El resultado se invierte
    return num_hex[::-1]

print(f"El número {num_dec2} es igual a {convertidor_hex(num_dec)}")