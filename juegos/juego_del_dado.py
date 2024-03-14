import random
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    puntaje_maquina=0
    puntaje_jugador=0
    nombre=input("cual es tu nombre",)
    print("Para tirar el dado debes apretar enter")
    while puntaje_maquina<30 and puntaje_jugador<30:
        input("tira el dado", )
        actual=random.randint(1,6)
        puntaje_jugador+=actual
        actual=random.randint(1,6)
        puntaje_maquina+=actual
        print("puntajes:")
        print("maquina: "+str(puntaje_maquina)+" "+str(nombre)+": "+str(puntaje_jugador))
    if puntaje_maquina>=30 and puntaje_jugador<30:
        ganador="maquina"
    elif puntaje_maquina<30 and puntaje_jugador>=30:
        ganador=nombre
    else:
        if puntaje_jugador>puntaje_maquina:
            ganador=nombre
        elif puntaje_jugador<puntaje_maquina:
            ganador="Maquina"
        else:
            ganador="empate"
    return ganador
print("El ganador es:",juego_del_dado())