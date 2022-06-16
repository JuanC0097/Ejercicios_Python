# Funcion en la cual se define un contador que iniciara en 0
# Se inicia un ciclo for que ira en un rango de 1 al numero ingresado por el usuario +1
# La variable i representa cada vuelta del ciclo, Ahora se pregunta 
# SI la variable i es igual a 1 O la variable i es igual al numero, nos saltaremos esta vuelta
# del ciclo "continue"
# SI NO NOS SALTAMOS LA VUELTA DEL CICLO PREGUNTAMOS 
#SI el numero divido por i (en este caso divido por dos, yaque nos saltamos la 1 vuelta del ciclo)
#es igual a cero el contador aumentara a +1 ,exponiendo que el numero no es primo
#Si el CONTADOR "maneja el resto de la divicion", es igual a 0 retornara True, SINO retornara false
def es_primo(numero):
    contador = 0

    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador +=1
    if contador == 0:
        return True
    else:
        return False


# Funcion que correra nuestro programa con un ciclo if, Dependiendo del valor que tome
#la variable es_primo imprimira si es verdadero o es falso
def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print(" Es primo")
    else:
        print(" No es primo")


if __name__== "__main__":
    run()

