def alta():
    cantidad = int(input("Ingrese la cantidad: "))
    precio = int(input("Ingrese el precio: "))
    compra = cantidad * precio
    compras.append(compra)

def baja():
    if len(compras) == 0:
        print("No hay compras realizadas hasta el momento.")
    else:
        cuento = 1
        print("Compras:")
        for i in compras:
            print(cuento,"-",i)
            cuento += 1
        elimino_num = int(input("Que compra desea eliminar?: "))
        elimino_num = elimino_num - 1
        for i in compras:
            if compras.index(i) == elimino_num:
                compras.remove(i)

def consulta():
    if len(compras) == 0:
        print("No hay compras realizadas hasta el momento.")
    else:
        print("La lista de compras hasta el momento es: ",compras)

def modificar():
    if len(compras) == 0:
        print("No hay compras realizadas hasta el momento.")
    else:
        cuento = 1
        print("Compras:")
        for i in compras:
            print(cuento,"-",i)
            cuento += 1
        modifico_num = int(input("Que compra desea modificar?: "))
        modifico_num = modifico_num - 1
        cantidad = int(input("Ingrese la cantidad: "))
        precio = int(input("Ingrese el precio: "))
        compra = cantidad * precio
        compras[modifico_num] = compra

compras = []
menu = 1
total = 0

print("Bienvenido al sistema de compras.")

while (menu != 0):
    print("1-Alta Compras\n2-Baja Compras\n3-Modificar Compras\n4-Consulta Compras\n0-Finalizar")
    menu = int(input("Que desea hacer?: "))
    if (menu == 1):
        alta()
    elif (menu == 2):
        baja()
    elif (menu == 3):
        modificar()
    elif (menu == 4):
        consulta()
    elif (menu == 0):
        menu = 0
        
for i in compras:
    total += i

if len(compras) == 0:
    print("No se han cargado compras.")
else:
    print("El total de la compra es: ", total)
    print("Las compras realizadas son: ", compras)