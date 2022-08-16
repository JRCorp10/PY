
def alta(cargar):
    cargar = int(input("Desea cargar cantidad y precio? (1-Si,2-No):"))
    return cargar

def baja(bajar):
    bajar = int(input("Desea borrar la carga de la compra? (1-Si,2-No):"))
    return bajar

def consulta():
    print("Hola Mundo")

def modificar():
    print("Hola Mundo")

compras = []
cargar = 0
bajar = 0
total = 0

while (alta(cargar) == 1):
    cantidad = int(input("Ingrese cantidad: "))
    compras.append(cantidad)
    precio = float(input("Ingrese precio: "))
    compras.append(precio)
    baja_si = baja(bajar)
    if (baja_si == 1):
        compras.remove(cantidad)
        compras.remove(precio)
    else:
        total = total + (cantidad*precio)
    

print("El total de la compra es: ", total)
print("Las compras realizadas son: ", compras)