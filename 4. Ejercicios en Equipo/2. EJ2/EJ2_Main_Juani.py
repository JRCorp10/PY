def f_acerto ():
    print("No has adivinado, tus chances se han acabado.")
    print("Los numeros ingresados fueron: ", user_num)
    print("El número era: ", random_num)

def f_noacerto():
    print("Los numeros ingresados fueron: ", user_num)
    print("El número era: ", random_num)

import random
random_num = random.randint(1,15)
user_num = []
contador_veces = 1
acerto = False

print("Juego para adivinar un número al azar del 1 al 15. Máximo 10 oportunidades de acertar.")

while (contador_veces <= 10):
    num = int(input("Ingrese un numero: "))
    user_num.append(num)
    if (num > random_num):
        print("Numero erroneo. Pista: Es menor al número ingresado.")
        contador_veces += 1
    elif (num < random_num):
        print("Numero erroneo. Pista: Es mayor al número ingresado.")
        contador_veces += 1
    else:
        print("Felicitaciones!!")
        print("Has acertado en",contador_veces,"intentos.")
        contador_veces = 11
        acerto = True

if (acerto == False):
    f_acerto()
else:
    f_noacerto()


