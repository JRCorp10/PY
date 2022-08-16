# Parametros no hace falta que sean iguales, función y maincode.
def añoscumplidos (años):
    años_ascendente = 1
    años_descendente = años
    print("Años cumplidos de forma descendente:")
    while años_descendente >= 1:
        print(años_descendente)
        años_descendente -= 1
    print("Años cumplidos de forma ascendente:")
    while años_ascendente <= años:
        print(años_ascendente)
        años_ascendente += 1

años = int(input("Cuantos años tiene?: "))
añoscumplidos(años)