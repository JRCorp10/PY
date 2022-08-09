""" programa que ingreses una fruta verdura o carne y la agregue a una lista, qué el comando VER te muestre la lista entera y finalizar """

"""# numero = input("poné un número: ")
# numero = int(numero) """

""" while (mientras) es un contador que va repitiendo los numeros acorde a lo qué le solicites """

verduras = []
frutas = []
carnes = []

pregunta = input("teclea si es FRUTA/VERDURA/CARNE o TERMINAR")
pregunta = str(pregunta)

while pregunta != ("terminar"):
    if pregunta == "verdura":
        x1 = input("¿Qué verdura es?: ")
        verduras.append(x1)

    if pregunta == "fruta":
        x2 = input("¿Qué fruta es?: ")
        frutas.append(x2)

    if pregunta == "carne":
        x3 = input("¿Qué carne es?: ")
        carnes.append(x3)

    pregunta = input("teclea si es FRUTA/VERDURA/CARNE o TERMINAR: ")
    pregunta = str(pregunta)

print("tenes las siguientes verduras: ", verduras)
print("tenes los siguientes cortes de carne: ", carnes)
print("tenes las siguientes frutas: ", frutas)
