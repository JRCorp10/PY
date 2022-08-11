def stock(cantidad,articulo):
    stock_cama = 1000
    stock_colchon = 1000
    stock_almohada = 1000

    if (articulo==1):
        stock_cama = stock_cama-cantidad
    elif (articulo==2):
        stock_colchon = stock_colchon-cantidad
    elif (articulo==3):
        stock_almohada = stock_almohada-cantidad 

def calculosyresultados_factura1(articulo,ef_tarj,cantidad,descuento,recargo,IVA,cama,colchon,almohada,factura1):
    # Hago Calculos
    if (articulo==1) and (ef_tarj==1):
        precio_final = ((cama*cantidad)*descuento)
    elif (articulo==1) and (ef_tarj==2):
        precio_final = (((cama*cantidad)*IVA)*recargo)

    if (articulo==2) and (ef_tarj==1):
        precio_final = ((colchon*cantidad)*descuento)
    elif (articulo==2) and (ef_tarj==2):
        precio_final = (((colchon*cantidad)*IVA)*recargo)

    if (articulo==3) and (ef_tarj==1):
        precio_final = ((almohada*cantidad)*descuento)
    elif (articulo==3) and (ef_tarj==2):
        precio_final = (((almohada*cantidad)*IVA)*recargo)

    # Muestro Resultados
    print("Datos de la factura")
    print("Nombre: ", factura1[0])
    print("Telefono: ", factura1[1])
    print("Dirección: ", factura1[2])
    print("DNI: ", factura1[3])
    print("Fecha de Venta: ", factura1[4])
    if (factura1[5] == 1):
        print("Punto de Venta: Salon")
    else:
        print("Punto de Venta: Tienda Online")
    if (factura1[6] == 1):
        print("Articulo: Cama")
    elif(factura1[6] == 2):
        print("Articulo: Colchon")
    else:
        print("Articulo: Almohada")
    print("Cantidad: ", factura1[7])
    if (factura1[8] == 1):
        print("Tipo: Efectivo")
    else:
        print("Tipo: Tarjeta")

    print("El total de su compra es: ", precio_final)
    print("Gracias por su compra, ", factura1[0])

def calculosyresultados_factura2(articulo,ef_tarj,cantidad,descuento,recargo,IVA,cama,colchon,almohada,factura2):
    # Hago Calculos
    if (articulo==1) and (ef_tarj==1):
        precio_final = ((cama*cantidad)*descuento)
    elif (articulo==1) and (ef_tarj==2):
        precio_final = (((cama*cantidad)*IVA)*recargo)

    if (articulo==2) and (ef_tarj==1):
        precio_final = ((colchon*cantidad)*descuento)
    elif (articulo==2) and (ef_tarj==2):
        precio_final = (((colchon*cantidad)*IVA)*recargo)

    if (articulo==3) and (ef_tarj==1):
        precio_final = ((almohada*cantidad)*descuento)
    elif (articulo==3) and (ef_tarj==2):
        precio_final = (((almohada*cantidad)*IVA)*recargo)

    # Muestro Resultados
    print("Datos de la factura")
    print("Nombre: ", factura2[0])
    print("Telefono: ", factura2[1])
    print("Dirección: ", factura2[2])
    print("DNI: ", factura2[3])
    print("Fecha de Venta: ", factura2[4])
    if (factura2[5] == 1):
        print("Punto de Venta: Salon")
    else:
        print("Punto de Venta: Tienda Online")
    if (factura2[6] == 1):
        print("Articulo: Cama")
    elif(factura2[6] == 2):
        print("Articulo: Colchon")
    else:
        print("Articulo: Almohada")
    print("Cantidad: ", factura2[7])
    if (factura2[8] == 1):
        print("Tipo: Efectivo")
    else:
        print("Tipo: Tarjeta")

    print("El total de su compra es: ", precio_final)
    print("Gracias por su compra, ", factura2[0])

def facturascargadas (factura_nombres):
    print("Las facturas cargadas son: ", factura_nombres)