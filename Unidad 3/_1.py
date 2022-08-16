Multiplo = 2
tres_veces = 1

while (tres_veces <= 3):
    x = int(input("Ingrese un numero: "))
    tres_veces = tres_veces + 1

    if x % Multiplo == 0:
        print("El número ingresado es",x, "y es par.")
    if x % Multiplo != 0:
        print("El número ingresado es",x,"y es impar.")
    
