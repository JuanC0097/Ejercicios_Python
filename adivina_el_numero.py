import random

def run():
    numero_aleatorio = random.randint(1 , 100)
    numero_elejido = int(input("elige un numero entre el 1 al 100: "))
    while numero_elejido != numero_aleatorio:
        if numero_elejido < numero_aleatorio:
            print(" busca un numero mas grande ")
        else:
            print("Busca un numero mas pequeño")
        numero_elejido = int(input("Elige otro numero: "))
    print ("Ganaste")


if __name__ == "__main__":
    run()