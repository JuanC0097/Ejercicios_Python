#Se define una COSTANTE limite para guarda el fin del bucle
#Se define una variable que iniciara en 0
#Se define una variable que guardara la potencia de 2 en la variable contador
def run():
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2 ** contador
    #Se inicia el bluce WHILE
    #El cual mientras potencia_2 sea menor a la costante LIMITE:
    #Imprimira un mensaje que retornara el valor donde se encuentra el contador + el resultado
    #de elevar el dos al contador
    while potencia_2 < LIMITE:
        print("2 elevado a: "+ str(contador)+ " es igual a: " + str(potencia_2))
        #Para que no se cree un bucle infinito, Se define que contador se ira sumando un 1 hasta llegar a 1000
        #Se define que la variable potencia_2 sera igual a 2 elevado al valor en el cual se encuentre el 
        #el contador
        contador = contador + 1
        potencia_2 = 2**contador


#Punto de partida
if __name__ =="__main__":
    run()