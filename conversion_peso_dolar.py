
#Se define una funcion con dos parametros
def conversor(tipo_pesos, valor_dolar):
    #Se recibira una entrada por consola con el numero de pesos pesos que se desean convertir
    peso = input("¿Cuantos pesos " +  tipo_pesos + " tienes?")
    #se convierte la variable peso a decimal
    peso = float(peso)
    #Operacion matematica de convercion 
    dolares = peso /valor_dolar
    #se define la variable dolare para que devuelva solamente dos valores decimales despues del .
    dolares = round(dolares, 2)
    #Se convierte la variable dolares a string
    dolares = str(dolares)
    #Se imprime en resultado total
    print("Tienes $" + dolares + " dolares")


#Creacion de la variable menu que recibira el tipo de moneda que se desea convertir
menu = ("""
Bienvenido al Convertidor de moneda 📱 

1. Pesos Colombianos
2. Pesos Argentinos
3. Pesos Mexicanos    
        """)
#Se crea la variable opcion, la cual guardara la eleccion del usuario
opcion = input(menu)

#Se valida la opcion del usuario con un ciclo if-elif-else
if opcion == ("1"):
    #Se realiza el llamado de la funcion conversor con los parametros de tipo_pesos -> colombianos y valor_dolar al valor del dolar en dicha moneda
    conversor("colombianos", 3875)
elif opcion == ("2"):
    #Se realiza el llamado de la funcion conversor con los parametros de tipo_pesos -> argentinos y valor_dolar al valor del dolar en dicha moneda
    conversor("argentinos", 65)
elif opcion == ("3"):
    #Se realiza el llamado de la funcion conversor con los parametros de tipo_pesos -> colombianos y valor_dolar al valor del dolar en dicha moneda
    conversor("mexicanos", 24)
else: 
    print("Por favor Ingrese una Opcion correcta")
