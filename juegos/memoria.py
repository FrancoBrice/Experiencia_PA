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
    time.sleep(3)

    number_list = [randint(0, 10) for i in range(5)]

    for number in number_list:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(number)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    for i in range(5):
        number_input = int(input(f"ingresa numero que apareciò en la posición: {i + 1}\n"))
        print("number_input", number_list[i])
        if number_input == number_list[i]:
            print("Correcto!")
        else: 
            print("incorrecto")
memoria()