from constants import settings
from service import ServiceTienda

class TiendaApp:
    def __init__(self):
        self.service = ServiceTienda()

    def run(self):
        while True:
            print(settings.MESSAGE_BIENVENIDA)
            menu = input(settings.MESSAGE_MENU_PRINCIPAL)

            if menu == "comprar" or menu == "vender":
                self.service.tienda_validation(menu)
            elif menu == "salirse":
                print(settings.MESSAGE_DESPEDIDA)
                break
            else:
                print("Opción no válida. Por favor, elija 'comprar', 'vender' o 'salirse'.")

if __name__ == "__main__":
    app = TiendaApp()
    app.run()