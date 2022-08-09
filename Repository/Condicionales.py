#IF

"""Sintaxis"""

#if (condición):
    # Bloque de instrucciones si se cumple la condición....
# Bloque de instrucciones fuera de la condición....

"""Ejemplo"""

resultado = int(input("¿Cuánto es 39 + 50?"))
if(resultado == 89):
    print("Respuesta Correcta. ¡Felicitaciones!")

"""-------------------------------------------------------------------------------------------------"""

#IF-ELSE

""" Sintaxis """

#if (condición):
    # Bloque de instrucciones si se cumple la condición....
#else:
    # Bloque de instrucciones si NO se cumple la condición....
# Bloque de instrucciones fuera de la condición....

"""Ejemplo"""

password = str(input("Ingrese la contraseña: "))

if(password == "35426491"):
    print("Contraseña correcta. Te damos la bienvenida.")
else:
    print("Contraseña incorrecta.")

"""-------------------------------------------------------------------------------------------------"""

#IF ANIDADOS

"""Ejemplo 1 """

password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
else:
    print('Tu contraseña es muy corta e insegura.')

    if (password != 'miClaveSegura'):
        print("Además, es incorrecta (por supuesto).")

      
"""Ejemplo 2"""

password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
elif (password != 'miClaveSegura'):
    print('Tu contraseña es muy corta e insegura.')
    print("Además, es incorrecta (por supuesto).")