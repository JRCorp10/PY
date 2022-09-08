compras = []

total = 0
cargar = int(input("Desea cargar cantidad y precio? (1-Si,2-No):"))

while (cargar == 1):
    cantidad = int(input("Ingrese cantidad: "))
    compras.append(cantidad)
    precio = float(input("Ingrese precio: "))
    compras.append(precio)
    total = total + (cantidad*precio)
    cargar = int(input("Desea continuar cargando cantidad y precio? (1-Si,2-No):"))

print("El total de la compra es: ", total)
print("Las compras realizadas son: ", compras)