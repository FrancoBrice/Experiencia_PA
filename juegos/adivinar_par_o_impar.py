def adivinar_par_o_impar(var):
    import random
    x = random.randint(1, 2)
    if x == 1:
        if str(var).lower == "impar":
            print("Correcto")
        else:
            print("Incorrecto")
    if x == 2:
        if str(var).lower == "par":
            print("Correcto")
        else:
            print("Incorrecto")
            
