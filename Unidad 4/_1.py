# Parametros no hace falta que sean iguales, función y maincode.
par_impar = lambda num: num % 2 == 0
ingreso_num = int(input("Ingrese un numero: "))

if par_impar(ingreso_num) == True:
    print("Su numero es par.")
else:
    print("Su numero es impar.")