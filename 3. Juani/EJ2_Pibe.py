import random

numerodeveces = 1
numerodeveces = int(numerodeveces)

numerorestantedeveces = 10
numerorestantedeveces = int(numerorestantedeveces)


numerorandom = random.randint(1,10)
numerorandom = int(numerorandom)

ganaste = 0
ganaste = int(ganaste)

ganasteen = 0
ganasteen = int(ganasteen)


while (numerodeveces <= 10) and (ganaste < 1): 
    numerodeveces = numerodeveces + 1
    numeroelegido= input("Adivina el número qué pensé del 1 al 10: ")
    numeroelegido=int(numeroelegido)

    if numeroelegido > 10:
            print("DEL 1 AL 10 DIJE MENSO DE MIERDA, TE CUENTA COMO CHANCE PERDIDA. perdón, me calmo.")
    
    if numeroelegido != numerorandom:
        numerorestantedeveces = numerorestantedeveces - 1
        print("No rey, te quedan", numerorestantedeveces , "mas, dale animate ")
        ganasteen = ganasteen + 1

    if numeroelegido == numerorandom:
        ganaste = ganaste + 1
        print("GANASTE" , "el numero era él: " , numerorandom , "adivinaste en: " , ganasteen , "chanses")

    
    if numerorestantedeveces == 0:
        print("mira que era facil adivinar idiota de mierda, preparate para que te tilde la pc por gordo boludo")