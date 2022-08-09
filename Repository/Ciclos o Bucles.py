#While

"""Sintaxis"""

#while(condición):
    #...
    #...
    # Bloque de instrucciones si se cumple la condición....
    # Dentro del while
    # Es sumamente importante cortar el while, sino el bucle es infinito.
    #...
    #...
# Bloque de instrucciones fuera de la condición....
# Fuera del while

"""Ejemplo 1 """

numero = float(input("Ingresa un número. 0 para terminar: "))

while(numero != 0):
    numero = float(input("Ingresa un número. 0 para terminar: "))

print("Fin del programa.")

"""Ejemplo 2 (Usando break) """

while(True):
    numero = float(input("Ingresa un número. 0 para terminar: "))
    if (numero == 0):
        break

print("Fin del programa.")

"""-------------------------------------------------------------------------------------------------"""

#For

"""Sintaxis"""

# for variable_contadora in range(valor_inicial, valor_final, tamaño_paso:
    #...
    #...
    #Bloque de instrucciones....
    #...
    #...
#Bloque de instrucciones fuera del ciclo...

"""Ejemplo 1 """# Contador 500 a 998 solo los pares.
for i in range(500, 1000, 2):
    print(i)

"""Ejemplo 2 """ # Contador 500 a 1000 solo los pares.
for i in range(500, 1000 + 1, 2):
    print(i)

"""Ejemplo 3 """ # Contador de 100 a 0.
for i in range(100, -1, -1):
    print(i)

"""Ejemplo 4 """
contador = 0 # Iniciamos el contador en cero
for i in range(100):
    contador += 1 # Aumentamos el contador en 1
print(contador)