from EJ1_Funciones_Juani import *

# Declaro Listas
factura_nombres = []
factura1 = []
factura2 = []

# Declaro Constantes del main
primer_factura = 0
cantidad_facturas = 1
precio_final = 0
precio_final = int(precio_final)
IVA = 1.21
recargo = 1.40
descuento = 0.9

# Inicio Programa
print("Bienvenido a Santu Compra")
print("Tenga en cuenta que el máximo de facturas posibles de cargar es 2.")
pregunta = input("Desea cargar una factura? (1=Si,2=No): ")
pregunta = int(pregunta)

while (pregunta == 1) and (cantidad_facturas <= 2):
    # Al menos cargo 1 factura.
    primer_factura = 1

    # Declaro Constantes del while    
    cama = 100
    colchon = 50
    almohada = 10

    # Declaro Variables del while
    nombre = str(input("Ingrese su nombre: "))
    if (cantidad_facturas == 1):
        factura_nombres.append(nombre)
        factura1.append(nombre)
    else:
        factura_nombres.append(nombre)
        factura2.append(nombre)
    telefono = int(input("Ingrese su telefono: "))
    if (cantidad_facturas == 1):
        factura1.append(telefono)
    else:
        factura2.append(telefono)
    direccion = str(input("Ingrese su dirección: "))
    if (cantidad_facturas == 1):
        factura1.append(direccion)
    else:
        factura2.append(direccion)
    dni = int(input("Ingrese su DNI: "))
    if (cantidad_facturas == 1):
        factura1.append(dni)
    else:
        factura2.append(dni)
    fecha_venta = int(input("Ingrese la fecha de compra (DDMMAAAA): "))
    if (cantidad_facturas == 1):
        factura1.append(fecha_venta)
    else:
        factura2.append(fecha_venta)
    punto_venta = int(input("Ingrese el punto de venta (1-Salon,2-Tienda Online): "))
    if (cantidad_facturas == 1):
        factura1.append(punto_venta)
    else:
        factura2.append(punto_venta)
    articulo = int(input("Ingrese número del artículo (1-Cama,2-Colchon,3-Almohada): "))
    if (cantidad_facturas == 1):
        factura1.append(articulo)
    else:
        factura2.append(articulo)
    cantidad = int(input("Ingrese la cantidad: "))
    if (cantidad_facturas == 1):
        factura1.append(cantidad)
        stock(cantidad,articulo)
    else:
        factura2.append(cantidad)
        stock(cantidad,articulo)
    ef_tarj = int(input("Ingrese tipo (1-Efectivo,2-Tarjeta): "))
    if (cantidad_facturas == 1):
        factura1.append(ef_tarj)
    else:
        factura2.append(ef_tarj)

    # Muestro factura cargada
    print("Su factura ha sido cargada correctamente.")

    # Cargo posible futura factura
    cantidad_facturas += 1

    # Pregunta si deseo continuar.
    pregunta = input("Desea cargar otra factura? (1=Si,2=No): ")
    pregunta = int(pregunta)

if (cantidad_facturas == 3):
    print("Ha llegado al máximo de facturas.")

if (primer_factura == 1):
    calculosyresultados(articulo,ef_tarj,cantidad,descuento,recargo,IVA,cama,colchon,almohada,nombre,telefono,direccion,dni,fecha_venta,punto_venta)
else:
    # No hay facturas cargadas
    print("No hay facturas cargadas.")