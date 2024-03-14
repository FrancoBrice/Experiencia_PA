from random import randint 
import time
import os

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("Recuerda los siguientes números:")
    number_list = [randint(0, 10) for i in range(5)]
    print(number_list)

    for number in number_list:
        print(number)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    for i in range(5):
        number_input = input("ingresa el primer numero\n")
        if number_input == number:
            print("Correcto!")
        else: 
            print("incorrecto")
memoria()