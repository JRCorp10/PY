# Parametros no hace falta que sean iguales, función y maincode.
frase_alrevez = lambda frase: frase[::-1]
ingreso_frase = str(input("Ingrese una frase: "))
print("La frase al reves es:", frase_alrevez(ingreso_frase))