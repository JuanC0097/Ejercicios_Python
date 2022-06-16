def run():
    #########################################################################################
    #Se utiliza continue para informar a python que si en dado caso la condicion
    #Si la variable al dividirla por dos es distinto a 0, saltara la vuelta del ciclo.
    #for contador in range(1000):
    #    if contador % 2 != 0:
    #        continue
    #    print(contador)

    #########################################################################################
    #Se utiliza break con cortador del codigo, para i en el rango de 0 a 99999, imprimira i
    #Si i es igual a 5678 break- el codigo se rompera alli.
    #for i in range (0,10000):
    #    print(i)
    #    if i == 5678:
    #        break
    ##########################################################################################

    texto = input("Ingrese un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__=="__main__":
    run()
