from compra import Compra
from venta import Vender
from constants import settings

class ServiceTienda():
    def __init__(self):
        self.compra = Compra()
        self.venta = Vender()

    def tienda_validation(self, menu: str):
        try:
          if menu in "comprar":
            self.compra.compra_iniciada()
          elif menu in "vender":
            self.venta.venta_iniciada()
          else:
            print(settings.MESSAGE_DESPEDIDA)
        except Exception as e:
            print(e)