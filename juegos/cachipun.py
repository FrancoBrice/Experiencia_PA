import random
def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    eleccion=int(input("Elije una opcion: piedra (1), tijera (2), Papel (3)",))
    maquina=random.randint(1,3) 
    print("La maquina eligio:", maquina)
    if maquina==eleccion:
        print("Empate")
    elif (eleccion==1 and maquina==2) or (eleccion==3 and maquina==1) or (eleccion==2 and maquina==3):
        print("ganaste")
    else:
        print("perdiste")

