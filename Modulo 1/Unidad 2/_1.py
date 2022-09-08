import  sys

Multiplo = 2

x1 = input("Ingrese primer valor: ")
x1 = int(x1)

x2 = input("Ingrese primer valor: ")
x2 = int(x2)

x3 = input("Ingrese primer valor: ")
x3 = int(x3)

if x1 % 2 == 0:
    print("El primer número ingresado",x1, "es múltiplo de 2.")
else:
    print("El primer número ingresado",x1,"no es múltiplo de 2.")

if x2 % 2 == 0:
    print("El segundo número ingresado",x2, "es múltiplo de 2.")
else:
    print("El segundo número ingresado",x2,"no es múltiplo de 2.")

if x3 % 2 == 0:
    print("El tercer número ingresado",x3, "es múltiplo de 2.")
else:
    print("El tercer número ingresado",x3,"no es múltiplo de 2.")