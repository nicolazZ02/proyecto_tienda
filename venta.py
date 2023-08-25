from constants import settings

class Vender():
    def __init__(self):
        pass

    def venta_iniciada(self):
        print(settings.MESSAGE_MODULO_VENDER)
        dep2 = int(input(settings.DEPOSITO_VENDER))

        while dep2 >= 1000000:
            nombre, documento, telefono, email = self.obtener_datos_cliente()
            cantidad_sal, cantidad_lentejas = self.obtener_cantidades_venta()
            total = self.calcular_descuento_venta(cantidad_sal, cantidad_lentejas)

            self.mostrar_recibo_venta(nombre, documento, telefono, email, total)

    def obtener_datos_cliente(self):
        nombre = input(settings.NOMBRE_APELLIDO)
        documento = input(settings.DOCUMENTO)
        telefono = input(settings.TELEFONO)
        email = input(settings.EMAIL)
        return nombre, documento, telefono, email

    def obtener_cantidades_venta(self):
        cantidad_sal = int(input(settings.VENTA_SAL))
        cantidad_lentejas = int(input(settings.VENTA_LENTEJAS))
        return cantidad_sal, cantidad_lentejas

    def calcular_descuento_venta(self, cantidad_sal, cantidad_lentejas):
        cantidad_sal_multiplicada = cantidad_sal * settings.PRECIOS[0]
        cantidad_lentejas_multiplicada = cantidad_lentejas * settings.PRECIOS[1]
        cantidad_sumada = cantidad_sal_multiplicada + cantidad_lentejas_multiplicada
        promedio_total = cantidad_sumada * 0.3
        total = cantidad_sumada - promedio_total
        return total

    def mostrar_recibo_venta(self, nombre, documento, telefono, email, total):
        print("El descuento por esta venta es:", total)
        print(settings.MESSAGE_VENTA_FINAL[0] + nombre, settings.MESSAGE_VENTA_FINAL[1] + documento,
              settings.MESSAGE_VENTA_FINAL[2] + telefono, settings.MESSAGE_VENTA_FINAL[3] + email,
              settings.MESSAGE_VENTA_FINAL[4] + str(total))