def ej3 (π,R):
    print("Ejercicio 3 - Unidad 1 con funciones.")
    P = 2 * π * R
    print("El perimetro de la circunferencia es: ", P)
    
def ej4 (π,R):
    print("Ejercicio 4 - Unidad 1 con funciones.")
    A = π * R * R
    print("El area de la circunferencia es: ", A)

def ej5 (Porc,N):
    print("Ejercicio 5 - Unidad 1 con funciones.")
    NPorc = N * Porc
    print("El numero incrementado en un 10% es: ", NPorc)

π = 3.1416
Porc = 1.1

R = input("Ingrese el radio de una circunferencia: ")
R = float(R)
ej3 (π,R)

R = input("Ingrese el radio de una circunferencia: ")
R = float(R)
ej4 (π,R)

N = input("Ingrese un número entero: ")
N = int(N)
ej5 (Porc,N)