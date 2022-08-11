from pickle import APPEND
from EJ1_FuncionesSantiySantuk import *

print("Bienvenido a Santu Compra")
pregunta = input("Desea cargar una factura? (1=Si,2=No): ")
pregunta = int(pregunta)


while pregunta == 1:

    nombre = input("Para comenzar, ingrese su nombre: ")

    telefono = input("Ingresa tu numero de telefono: ")

    direccion = input("Ingrese su direccion:")

    dni = input("Ingrese DNI: ")

    fechaventa = input("Ingrese fecha(dd/mm/aaaa): ")

    puntoventa = input("Ingrese punto de venta( salon/online ): ")

    cantidad = input(
        "Ingrese cantidad( compra maxima 1000 unidades 1/10000 ): ")
    cantidad = int(cantidad)

    aarticulo = input("Ingrese el articulo deseado( colchon/cama/almohada ): ")
    aarticulo = str(aarticulo)

    if aarticulo == "colchon":
        articulo = pcolchon

    if aarticulo == "cama":
        articulo = pcama

    if aarticulo == "almohada":
        articulo = palmohada

    formapago = input("Ingrese forma de pago ( efectivo/tarjeta ): ")

    if formapago == "tarjeta":
        pagotarjeta(cantidad, articulo, tarjeta)

    if formapago == "efectivo":
        pagoefectivo(cantidad, articulo, descuento)

if pregunta = input("Desea cargar otra compra? (1=Si,2=No): ")
pregunta == 1
numerodecompras.append()


"""print("Punto de venta:", puntoventa)
print("Forma de pago: ", formapago)
print("El total de su compra es: ", totalconrecargo)
print("Gracias por su compra, ", nombre)
print("Valla a jugar Argentun tranquilo, mhijo")
"""


if pregunta == 2:
    print("Lo esperamos cuando guste, ", nombre)

# print cantidad >1000 se entrega en 48hs
