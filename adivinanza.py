
import random

numero_secreto = random.randint(1,100)
adivinado = False

print ("Bienvenido al Juego")
while not adivinado:
    entrada = input ("Introduce nro del 1 al 100: ")
    numero = int(entrada)
    if numero == numero_secreto:
        print ("Felicitaciones")
        adivinado = True
    elif numero < numero_secreto:
        print ("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
