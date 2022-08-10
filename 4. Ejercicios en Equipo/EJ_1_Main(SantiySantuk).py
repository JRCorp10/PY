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

    articulo = input("Ingrese el articulo deseado( colchon/cama/almohada ): ")
    articulo = str(articulo)

    # Valores articulos
    cama = 100
    cama = int(cama)
    colchon = 50
    colchon = int(colchon)
    almohada = 10
    almohada = int(almohada)

    cantidad = input("Ingrese cantidad( compra maxima 10 unidades 1/10 ): ")
    cantidad = int(cantidad)

    if articulo == "colchon":
        articulomascantidad = cantidad * colchon
    if articulo == "cama":
        articulomascantidad = cantidad * cama
    if articulo == "almohada":
        articulomascantidad = cantidad * almohada

    formapago = input("Ingrese forma de pago ( efectivo/tarjeta ): ")

    # valores iva y tarjeta
    contado = 0.9
    contado = int(contado)
    iva = 1.21
    iva = float(iva)
    recargotarjeta = 1.4
    recargotarjeta = float(recargotarjeta)

    if formapago == "tarjeta":
        totalconrecargo = articulomascantidad * recargotarjeta * iva
    if formapago == "efectivo":
        totalconrecargo = articulomascantidad * contado
    pregunta = input("Desea cargar otra factura? (1=Si,2=No): ")
print(
    "Datos del comprador:",
    ("Nombre: ", nombre),
    ("Telefono: ", telefono),
    ("Direccion: ", direccion),
    ("DNI: ", dni),
)
print("Punto de venta:", puntoventa)
print("Forma de pago: ", formapago)
print("El total de su compra es: ", totalconrecargo)
print("Gracias por su compra, ", nombre)
print("Valla a jugar Argentun tranquilo, mhijo")


if pregunta == 2:
    print("Lo esperamos cuando guste, ", nombre)