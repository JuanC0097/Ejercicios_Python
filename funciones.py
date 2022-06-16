###############################
# Se crea la funcion imprimir mensaje
#def imprimir_mensaje():
# Informa a python que pasos seguira la funcion
 #   print("Mensaje especial")
#print("aprendiendo funciones")

#Se realiza el llamado de las funciones
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

#Se define la funcion conversacion que recibira como parametros la variable mensaje
#def conversacion(mensaje):
#Se definen los pasos a seguir en la funcion convesacion
#    print("hola")
#    print(mensaje)
#    print("adios")
#------------------------------------------------------

#Se recibe la entrada tipo entero por medio del input 
#opcion = int(input("Eliga una opcion (1,2,3): "))

#Se define la estructura if-elif-else, la cual definira que camino tomara nuestro codigo, dependiendo de la entrada.
#if opcion == 1:
#Se realiza el llamado de la funcion conversacion TENER EN CUENTA QUE EN LOS PARAMETROS DE CONVERSACION LA FUNCION MENSAJE CAMBIARA DEPENDIENDO DE LA OPCION DEL USUARIO.
#    conversacion("elegiste la opcion 1")
#elif opcion == 2:
#    conversacion("elegiste la opcion 2")
#elif opcion == 3:
#    conversacion("elegiste la opcion 3")
#else:
#    print("Por favor ingresa un valor adecuado")


######################################################

#Se la funcion suma con los parametro a y b
def suma(a, b):
    #Pasos a seguir por la funcion
    print("Se suman dos valores")
    #Operacion matematica encargada de sumar los parametros
    resultado = a + b
    #Palabra clave encargada de retornar el valor de la variable resultado
    return resultado
#se crea una nueva variable que guardara el valor de suma de dos valores
sumatoria = suma(4, 5)
#imprime en pantalla el valor de sumatoria
print(sumatoria)

