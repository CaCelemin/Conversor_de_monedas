menu = """
Bienvenido al conversor de Monedas 🌌

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción:  """ 

opcion = int(input (menu))

def conversor (tipo_pesos, valor_dolar):
    pesos = input ("¿Cuantos pesos "+ tipo_pesos + " tienes?: ")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2) 
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dólares")    


if opcion == 1:
    conversor ("Colombianos", 3875)
elif opcion == 2:
    conversor ("Argentinos", 65)
elif opcion == 3:
    conversor ("Mexicanos", 24)
else:
    print ("Ingresa una opción correcta por favor!")


# pesos = input ("¿Cuantos pesos Colombianos tienes?: ")
# pesos = float (pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round (dolares, 2) # la función road es para reducir decimales, para este caso solo quiero 2 #
# dolares = str (dolares)
# print ("Tienes $" + dolares + " dólares")