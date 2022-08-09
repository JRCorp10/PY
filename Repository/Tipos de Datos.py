""" Número Entero (int)
Este tipo de dato se corresponde con números enteros, es decir, sin parte decimal.

Número Decimal (float)
Este tipo de dato se corresponde con números reales con parte decimal. Cabe destacar que el separador decimal en Python es el punto (.) y no la coma (,).

Número Complejos (complex)
Nos sirven para representar números complejos, con una parte real y otra imaginaria. Como hemos visto en la unidad anterior son tipos de datos inmutables.

Caracter (chr)
Este tipo de dato se corresponde con un símbolo tipográfico, es decir, una letra, número, coma, espacio, signo de punutación, etc.

Cadena de Texto (str)
Este tipo de datos se corresponde con una cadena de caracteres.

Booleano (bool)
Este tipo de dato reconoce solamente dos valores: Verdadero (True) y Falso (False)"""

# Int
entero = 1
entero = int(entero)  

# Float
decimal = 5.3
decimal = float(decimal)

# Complex
decimal = 5.3
decimal = complex(decimal)

# Chr
character = "A"
character = chr(character)

# Str
string = "Juan Ignacio Ruiz"
string = str(string)

# Bool
booleano = "FALSE" or "TRUE"
booleano = bool(booleano)

# Ejemplos

entero = 80
decimal = 6.14159
caracter = 'Q'
cadena = 'Análisis Numérico'
booleano = True

print(int(decimal)) # Daría como resultado = 6
print(int(True)) # Daría como resultado = 1
print(int(False)) # Daría como resultado = 0

print(float(entero)) # Daría como resultado = 80.0
print(float(True)) # Daría como resultado = 1.0
print(float(False)) # Daría como resultado = 0.0