# Declaro Constantes del main
primer_factura = 0
precio_final = 0
precio_final = int(precio_final)
IVA = 1.21
recargo = 1.40

# Inicio Programa
print("Bienvenido a Santu Compra")
pregunta = input("Desea cargar una factura? (1=Si,2=No): ")
pregunta = int(pregunta)

while (pregunta == 1):
    # Al menos cargo 1 factura.
    primer_factura = 1

    # Declaro Constantes del while    
    cama = 100
    colchon = 50
    almohada = 10

    # Declaro Variables del while
    nombre = str(input("Ingrese su nombre: "))
    telefono = int(input("Ingrese su telefono: "))
    direccion = str(input("Ingrese su dirección: "))
    dni = int(input("Ingrese su DNI: "))
    fecha_venta = int(input("Ingrese la fecha de compra (DDMMAAAA): "))
    punto_venta = int(input("Ingrese el punto de venta (1-Salon,2-Tienda Online): "))
    articulo = int(input("Ingrese número del artículo (1-Cama,2-Colchon,3-Almohada): "))
    cantidad = int(input("Ingrese la cantidad: "))
    ef_tarj = int(input("Ingrese tipo (1-Efectivo,2-Tarjeta): "))

    # Muestro factura cargada
    print("Su factura ha sido cargada correctamente.")

    # Pregunta si deseo continuar.
    pregunta = input("Desea volver a cargar la factura? (1=Si,2=No): ")
    pregunta = int(pregunta)

if (primer_factura == 1):
    # Hago Calculos
    if (articulo==1) and (ef_tarj==1):
        precio_final = cama*cantidad
    elif (articulo==1) and (ef_tarj==2):
        precio_final = (((cama*cantidad)*IVA)*recargo)

    if (articulo==2) and (ef_tarj==1):
        precio_final = colchon*cantidad
    elif (articulo==2) and (ef_tarj==2):
        precio_final = (((colchon*cantidad)*IVA)*recargo)

    if (articulo==3) and (ef_tarj==1):
        precio_final = almohada*cantidad
    elif (articulo==3) and (ef_tarj==2):
        precio_final = (((almohada*cantidad)*IVA)*recargo)

    print("Datos de la factura")
    print("Nombre: ", nombre)
    print("Telefono: ", telefono)
    print("Dirección: ", direccion)
    print("DNI: ", dni)
    print("Fecha de Venta: ", fecha_venta)
    if (punto_venta == 1):
        print("Punto de Venta: Salon")
    else:
        print("Punto de Venta: Tienda Online")
    if (articulo == 1):
        print("Articulo: Cama")
    elif(articulo == 2):
        print("Articulo: Colchon")
    else:
        print("Articulo: Almohada")
    print("Cantidad: ", cantidad)
    if (ef_tarj == 1):
        print("Tipo: Efectivo")
    else:
        print("Tipo: Tarjeta")

    print("El total de su compra es: ", precio_final)
    print("Gracias por su compra, ", nombre)
else:
    print("No hay facturas cargadas.")