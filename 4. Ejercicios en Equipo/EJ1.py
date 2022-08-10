"""
Crear un programa que pida por terminal:
    - Nombre
    - Telefono
    - Dirección
    - DNI
    - FECHA DE VENTA
    - PUNTO DE VENTA (Salon o Tienda Online)
    - ARTICULO (1,2,3)
    - CANTIDAD
    - PRECIO UNITARIO
    - EFECTIVO o TARJETA

    Preguntar si desea iniciar el programa y preguntar si desea volver a cargar la factura o finalizar.
    Mostrar:
        - Ticket con datos de la compra.
        - Si paga en efectivo no se le agrega el IVA, si paga con tarjeta se le suma el IVA y un 40%.
        - Cuanto debe pagar (Teniendo en cuenta que los precios están sin IVA, debemos sumarle el IVA)
        - Al final del programa debe decir "Gracias por su compra y el nombre del comprador".
"""


"""
    Modifique el ejercicio anterior para que la persona pueda ingresar hasta un máximo de 10 facturas.
    Usar al menos 4 funciones, cada una de ellas tiene que tener un proposito.
    Todas las funciones deben estar en un archivo separado y ser llamadas desde el archivo main del código.
    Una función debe representar el stock de los 3 items (Todos inicializados en 1000):
        - Cada vez que se carga una factura debe restar la cantidad comprada.
        - En caso de que el stock sea 0, debe informar al final, un mensaje que diga "Sin stock, su producto llegará en el transcuro de las 48hs a su domicilio.".
    Una vez finalizada la carga de facturas:
        - Mostrar la/s factura/s cargadas por NOMBRE y un ID único.
        - Dar la opción de mostrar dichas las facturas hasta que la persona desee finalizar.
    Mostrar:
        - Todo lo mismo que en el ejercicio anterior.
        - En caso de pagar en efectivo se aplicara un descuento del 10%.
        - Mostrar stock remanente o mensaje depende el caso.
"""