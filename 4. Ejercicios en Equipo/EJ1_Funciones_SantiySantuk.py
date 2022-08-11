# numero de compras

numerodecompras = [0]
numerodecompras = int(numerodecompras)


# precios

pcama = 100
pcama = int(pcama)

pcolchon = 50
pcolchon = int(pcolchon)

palmohada = 10
palmohada = int(palmohada)


# stock inicial

stockinicialcama = 1000
stockinicialcama = int(stockinicialcama)

stockinicialalmohada = 1000
stockinicialalmohada = int(stockinicialalmohada)

stockinicialcolchon = 1000
stockinicialcolchon = int(stockinicialcolchon)

# medios de pago

descuento = 0.9
tarjeta = 1.61


def pagoefectivo(cantidad, articulo, descuento):
    finalcosto = cantidad * articulo * descuento
    finalcosto = float(finalcosto)
    print("el precio final es: ", finalcosto)


def pagotarjeta(cantidad, articulo, tarjeta):
    finalcosto = cantidad * articulo * tarjeta
    print("el precio final es", finalcosto)
