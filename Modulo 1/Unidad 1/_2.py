# Modulo Sys
import  sys

Multiplo = 2

x1 = input("Ingrese primer valor: ")
x1 = int(x1)
x1 = x1 % Multiplo

x2 = input("Ingrese primer valor: ")
x2 = int(x2)
x2 = x2 % Multiplo

x3 = input("Ingrese primer valor: ")
x3 = int(x3)
x3 = x3 % Multiplo

print("Se indica con 0 si es múltiplo de 2 y con 1 si no lo es.")
print("El primer valor resulta: ", x1)
print("El segundo valor resulta: ", x2)
print("El tercer valor resulta: ", x3)