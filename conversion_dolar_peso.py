#Se recibe una entrada con input
dolar = input("¿Cuantos dolares Tienes?")
#Se convierte la entrada a un tipo de dato decimal
dolar = float(dolar)
# Se defina la variable con el valor de peso
peso = 3935
#Se realiza la operacion matematica para hallar la convercion del dolar a peso
pesos = dolar* peso
# Por medio de round se define que la variable pesos  solo devolvera un valor decimal con 2 digitos despues del .
pesos = round(pesos, 2)
#Se convierte la variable pesos a un dato tipo string
pesos = str(pesos)
# se imprime el resultado utilizando una concatenacion de dos strings y la variable pesos
print("Tienes: " + pesos + " Pesos Colombianos") 
