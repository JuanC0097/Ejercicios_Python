#Funcion encargada de:
#1. Reemplazar los espacios de nuestra entrada a una cadena vacia
#2. Crear la variable palabra_invertida, la cual hara un recorrido inverso de nuestra palabra
#3. Su logica se encargara de retornar el valor de palabra invertida. Dependiendo
#Si es verdadero o falso
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#Funcion encargada de correr el programa al inicio
#Esta logica se encargara de decidir si la palabra es un palindromo o no, y devolvera por consola
#El valor
def run():
    palabra = input("Escribe una palabra ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


#Punto de entrada. Correra las funciones que se encuentren dentro de esta
if __name__ == "__main__":
    run()
