import random

#Se utiliza una funcion que guardara 4 listas de caracteres
def generar_contraseña():
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    simbolos = ["@","?","¿","!","$","%","&","/","(","=","}","{","_","-","*","+",":",".",",",";","[","`"]
    numero = ["1","2","3","4","5","6","7","8","9","0"]
    #Se establece una variable que guardara las listas anteriores
    caracteres = mayusculas + minusculas + simbolos + numero
    #Se crea una lista vacia que mas adelante albergara la contraseña
    contraseña = []
    #Por medio del bucle for, se crea una variable que guardara los caracteres ramdom de la lista caracteres
    for i in range(15):
        caracter_ramdom = random.choice(caracteres)
        contraseña.append(caracter_ramdom)


    contraseña = "".join(contraseña)
    return contraseña


def run():
    contrasena = generar_contraseña()
    print("Tu nueva contraseña es:" + contrasena)

if __name__ == "__main__":
    run()
