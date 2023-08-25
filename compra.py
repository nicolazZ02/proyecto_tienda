from constants import settings

class Compra():
    def __init__(self):
        pass

    def compra_iniciada(self):
        print(settings.MESSAGE_MODULO_COMPRAR)
        dep = int(input(settings.DEPOSITO))

        if dep >= 300000:
            nombre, documento, telefono, email = self.obtener_datos_cliente()
            producto = self.seleccionar_producto()
            cantidad, precio_total = self.calcular_precio_total(producto)

            if precio_total > 1000000:
                precio_total -= 30000

            self.mostrar_recibo(nombre, documento, telefono, email, precio_total)

    def obtener_datos_cliente(self):
        nombre = input(settings.NOMBRE_APELLIDO)
        documento = input(settings.DOCUMENTO)
        telefono = input(settings.TELEFONO)
        email = input(settings.EMAIL)
        return nombre, documento, telefono, email

    def seleccionar_producto(self):
        print(settings.PRODUCTOS_DISPONIBLES)
        return input(settings.SELECCION_PRODUCTO)

    def calcular_precio_total(self, producto):
        if producto == settings.ARTICULO[0]:
            cantidad = int(input(settings.CANTIDAD_SAL))
            precio_total = cantidad * settings.PRECIOS[0] / 1.15 * 0.15
        elif producto == settings.ARTICULO[1]:
            cantidad = int(input(settings.CANTIDAD_LENTEJAS))
            precio_total = cantidad * settings.PRECIOS[1] / 1.15 * 0.15
        else:
            cantidad = 0
            precio_total = 0
        return cantidad, precio_total

    def mostrar_recibo(self, nombre, documento, telefono, email, precio_total):
        print(settings.MESSAGE_COMPRA[0] + nombre, settings.MESSAGE_COMPRA[1] + documento,
              settings.MESSAGE_COMPRA[2] + telefono, settings.MESSAGE_COMPRA[3] + email,
              settings.MESSAGE_COMPRA[4] + str(precio_total))