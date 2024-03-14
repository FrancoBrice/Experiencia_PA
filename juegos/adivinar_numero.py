import random
import os


def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    number = random.randint(0, 10)
    input_user = int(input("adivina el número del 1 al 10\n"))
    if input_user == number:
        print("Correcto!") 
    else:
        print("No es correcto")
    
