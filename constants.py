class Constants():
    ARTICULO=["Sal", "Lentejas"]
    PRECIOS= [500000 / 1.15 * 0.15, 700000 / 1.15 * 0.15]
    
    MESSAGE_BIENVENIDA="Bienvenido a nuestra tienda"
    MESSAGE_MENU_PRINCIPAL = "Que accion quiere hacer: comprar o vender o salirse \r\n"

    MESSAGE_MODULO_COMPRAR = "Has seleccionado el modulo de comprar"
    DEPOSITO= "Para iniciar deposite un valor mayor de 300 mil pesos \r\n"
    NOMBRE_APELLIDO="por favor ingrese nombre y apellido: \r\n"
    DOCUMENTO="Por favor digite su numero de documento: \r\n"
    TELEFONO="por favor ingrese su telefono: \r\n"
    EMAIL="por favor ingrese su correo: \r\n"

    PRODUCTOS_DISPONIBLES=  "los productos que estan disponibles: \r\n", ARTICULO[0], ARTICULO[1]
    SELECCION_PRODUCTO="Cual de los productos desea llevar \r\n"
    MESSAGE_COMPRA_INITIAL="Empieza tu compra"

    CANTIDAD_INITIAL= "Escriba la cantidad que desea llevar \r\n"
    CANTIDAD_SAL= "Escriba la cantidad de sal que desea llevar \r\n"
    CANTIDAD_LENTEJAS= "Escriba la cantidad de lentejas que desea llevar \r\n"


    MESSAGE_COMPRA=["Nombre cliente:", "Numero de documento:", "Telefono del cliente:", "Correo del cliente:", "Cantidad total con IVA:",]
    MESSAGE_COMPRA_NO=["Nombre cliente:" , "Numero de documento:","Telefono del cliente:","Cantidad total con IVA:",]
    

    DEPOSITO_VENDER = "Para inicar deposite un valor mayor a 1 millon de pesos \r\n"
    MESSAGE_MODULO_VENDER = "Has seleccionado el modulo de vender"
    SELECCION_PRODUCTO_COMPRA="Cual de los productos desea llevar \r\n"
    MESSAGE_SEGUIR_COMPRANDO = "¿Quiere seguir comprando? \r\n"
    VAR_SI = "si"
    VAR_NO = "no"
    MESSAGE_PRODUCTOS_VENDER = "¿Cuantos productos quiere vender?"
    VENTA_SAL= "Escriba la cantidad que desea vender \r\n"
    VENTA_LENTEJAS= "Escriba la cantidad que desea vender \r\n"
    MESSAGE_VENTA_FINAL =["nombre cliente:","numero de documento:", "Telefono del cliente:", "Correo del cliente:", "venta con descuento:",]



    MESSAGE_CANTIDADES_AÑADIDAS= "¿Quiere pedir mas cantidades?", "Estos son los productos que hay disponibles", ARTICULO[0], PRECIOS[0], ARTICULO[1],PRECIOS[1]
    MESSAGE_DESPEDIDA = "Muchas gracias por estar en nuestra tienda y que vuelva muy pronto"
   

settings = Constants()