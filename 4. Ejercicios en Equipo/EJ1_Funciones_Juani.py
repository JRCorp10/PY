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

def calculosyresultados(articulo,ef_tarj,cantidad,descuento,recargo,IVA,cama,colchon,almohada,nombre,telefono,direccion,dni,fecha_venta,punto_venta):
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

def funcion4(factura_nombres):
    print(factura_nombres)