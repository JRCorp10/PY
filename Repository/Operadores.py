"""Operadores Aritméticos"""

# +	Realiza suma entre los operandos -- 12 + 3 = 15
# -	Realiza resta entre los operandos -- 12 - 3 = 9
# *	Realiza multiplicación entre los operandos -- 12 * 3 = 36
# /	Realiza División entre los operandos -- 12 / 3 = 4
# %	Realiza un módulo entre los operandos -- 16 % 3 = 1
# ** Realiza la potencia de los operandos -- 12 ** 3 = 1728
# // Realiza la división con resultado de número entero

"""Operadores Relacionales"""
# >	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	12 > 3 , devuelve True
# <	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	12 < 3 , devuelve False
# == Devuelve True si ambos operandos son iguales 12 == 3 , devuelve False
# >= Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha 12 >= 3 , devuelve True
# <= Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda 12 <= 3 , devuelve False
# != Devuelve True si ambos operandos no son iguales

"""Operadores de Asignación"""
# =	a = 5. El valor 5 es asignado a la variable a
# += a += 5 es equivalente a a = a + 5
# -= a -= 5 es equivalente a a = a - 5
# *= a *= 3 es equivalente a a = a * 3
# /= a /= 3 es equivalente a a = a / 3
# %= a %= 3 es equivalente a a = a % 3
# **= a **= 3 es equivalente a a = a ** 3
# //= a //= 3 es equivalente a a = a // 3
# &= a &= 3 es equivalente a a = a & 3
# |= a |= 3 es equivalente a a = a | 3
# ^= a ^= 3 es equivalente a a = a ^ 3
# >>= a >>= 3 es equivalente a a = a >> 3
# <<= a <<= 3 es equivalente a a = a << 3

"""Operadores Lógicos"""
# and Devuelve True si ambos operandos son True
# or Devuelve True si alguno de los operandos es True
# not Devuelve True si alguno de los operandos es False

"""Operadores de Pertenencia"""
# in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
# not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.
# Contiene World el string str?
mensaje = "Hello World"
print("World") in mensaje # Muestra True
# Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print("world") in mensaje # Muestra False  
print("codigo") not in str # Muestra True

"""Operadores de Identidad"""
# is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.
# is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.
a = 3
b = 3  
c = 4
print(a) is b # muestra True
print(a) is not b # muestra False
print(a) is not c # muestra True

""" Métodos principales de listas """

lista = [3,5,12,"Pepe"]

# Métodos de inserción: append, extend, insert
lista.append() # Agrega valor a la lista
lista = [1,2,3]
lista.append(4)
lista[1, 2, 3, 4] # Así queda la lista

lista.extend() # Agrega lista a una lista
lista2 = [5,6]
lista.extend(lista2)
lista[1, 2, 3, 4, 5, 6] # Así queda la lista

lista.insert() # Agrega valores a una lista
lista.insert(1,100)
lista[1, 100, 2, 3, 4, 5, 6] # Así queda la lista

# Métodos de eliminación: pop, remove
lista.pop()
lista.pop(6) # Quita el número 6 de la lista porque lista[6] = 6
lista[1, 100, 2, 3, 4, 5] # Así queda la lista

lista.pop(1) # Quita el número 100 de la lista porque lista[6] = 100
lista[1, 2, 3, 4, 5] # Así queda la lista

lista.remove()
lista.remove(3) # Quita el número 3 de la lista.
lista[1, 2, 4, 5] # Así queda la lista.

lista.copy() # Copia la lista.
lista.sort() # Ordena la lista.
lista.clear() # Limpia valores de la lista.
lista.count() # Cuenta cantidad de items en la lista.
lista.index() # Devuelve posición del puntero o índice.
lista.reverse() # Corre la lista de atrás hacía delante.