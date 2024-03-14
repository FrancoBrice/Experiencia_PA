import random
import os


def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    input_user = input("Adivina si el número es par o impar\n"
                       "ingresa la palabra par o impar: ")
    x = random.randint(1, 10)
    if x%2 != 0:
        if str(input_user).lower() == "impar":
            print("Correcto")
        else:
            print("Incorrecto")
    elif x%2 == 0:
        if str(input_user).lower() == "par":
            print("Correcto")
        else:
            print("Incorrecto")
            
