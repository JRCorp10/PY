def funcion(x1,x2):
    # Bloque de instrucciones
    valor = x1 + x2
    return valor

def procedimiento(n, nombre):
    # Bloque de instrucciones
    if(n == 0):
        print("Hola ", nombre)
        return
    print("Adiós ", nombre)

x1 = 2
x2 = 15
n= 1
nombre = "Juani"

funcion(x1,x2) # Así llamo a la función.
procedimiento(n,nombre) # Así llamo al procedimiento.