#       EJERCICIO 1

# Escribe un algoritmo que, dada una cantidad de dinero en euros, determine la menor cantidad de billetes de cada denominación que se puede entregar.Teniendo en cuenta que hay billetes de 500,200,100,50,20,10 y 5 € y monedas de 2 y 1 €


#Listado de billetes
billetes = [500, 200, 100, 50, 20, 10, 5]

#listado de monedas
monedas = [2,1]

#Ingreso de la cantidad de dinero en euros por parte del usuario
cantidad_dinero = int(input("Ingrese una cantidad de dinero: "))

#Mientras la cantidad de dinero sea mayor a 500 descontará billetes
while(cantidad_dinero>500):
    #Recorre el listado de billetes
    for bill in billetes:
        acumulador = 0
        #mientras la cantidad de dinero sea mayor o igual a la denominación del billete, este descontará y aumentará el acumulador
        while cantidad_dinero>=bill:
            cantidad_dinero -= bill
            acumulador +=1
        #Si se ejecutó al menos una vez el while anterior significa que tendrá que imprimir el billete que usó
        if acumulador > 0:
            print(f"{acumulador} billete(s) de {bill}€")

#Mientras la cantidad de dinero sea mayor a 0 después de haber pasado por los billetes, se descontará monedas
while(cantidad_dinero>0):
    #Recorre el listado de monedas
    for coin in monedas:
        acumulador = 0
        #mientras la cantidad de dinero sea mayor o igual a la denominación de la moneda, este descontará y aumentará el acumulador
        while cantidad_dinero>=coin:
            cantidad_dinero -= coin
            acumulador += 1
        #Si se ejecutó al menos una vez el while anterior significa que tendrá que imprimir el billete que usó
        if acumulador > 0:
            print(f"{acumulador} moneda(s) de {coin}€")
    
