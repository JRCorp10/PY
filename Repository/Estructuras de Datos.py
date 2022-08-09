"""
Listas

Se trata de conjuntos ordenados de elementos, encerrados por corchetes y separados por comas. 
El orden comienza con el índice 0 para el primer lugar de la lista.
Índice es la posición en la cual está el puntero."""
i = 2
lista = [10,20,30,40]
print(lista[i]) # Daría como resultado = 30
"""Pueden agruparse valores de distintos tipos de datos básicos, y es posible agregar, eliminar o modificar elementos de las listas en cualquier momento."""

# Definición de una lista y referencia a un índice
lista = [10,20,30,40]
print(lista) # Daría como resultado = [10,20,30,40]
print(lista[0]) # Daría como resultado = 10
print(lista[3]) # Daría como resultado = 40

# Modificación de una lista
lista[1] = 25
print(lista) # Daría como resultado = [10,25,30,40]

# Generación de porciones a partir de una lista
sublista = lista[1:3]
print(lista) # Daría como resultado = [10, 25, 30, 40]
print(sublista) # Daría como resultado = [25, 30]
print(lista[:-1]) # Daría como resultado = [10, 25, 30]
print(lista[:]) # Daría como resultado = [10, 25, 30, 40]

""" 
Tuplas

Las Tuplas son básicamente listas de elementos estáticas, es decir, que no pueden modificarse. 
Para su definición, en lugar de corchetes se encierran valores separados por comas entre paréntesis."""

# Definición de una tupla y referencia a un índice
tupla = (6, 7, 8,9)
print(tupla) # Daría como resultado = (6, 7, 8, 9)
print(tupla[0]) # Daría como resultado = 6
print(tupla[3]) # Daría como resultado = 9

# Generación de porciones a partir de una tupla
subtupla = tupla[1:3]
print(tupla) # Daría como resultado = (6, 7, 8, 9)
print(subtupla) # Daría como resultado = (7, 8)
print(tupla[:-1]) # Daría como resultado = (6, 7, 8)
print(tupla[:]) # Daría como resultado = (6, 7, 8, 9)

# La similitud entre Listas y Tuplas es tan explícita que se puede bloquear una lista tranformándola en una tupla con la función tuple() o bien desbloquear una tupla para transformarla en una lista con la función list()
print(tuple(lista)) # Daría como resultado = (10, 25, 30, 40)
print(list(tupla)) # Daría como resultado = [6, 7, 8, 9]

"""
Diccionarios

En los Diccionarios cada elemento se compone de un par clave-valor, y para su definición es necesario encerrar los elementos entre llaves.
Es posible acceder a un valor utilizando su clave, pero no al revés.
Por este motivo, no se pueden repetir las claves para elementos distintos, pero sí es posible agregar, eliminar o modificar valores (Los diccionarios son mutables)."""

# Definición de un diccionario
diccionario = {"Codigo":7512,"Materia":"Análisis Numérico I"}
print(diccionario) # Daría como resultado = {'Codigo': 7512, 'Materia': 'Análisis Numérico I'}

# Referencia a un índice
print(diccionario["Codigo"]) # Daría como resultado = 7512
print(diccionario["Materia"]) # Daría como resultado = Análisis Numérico I