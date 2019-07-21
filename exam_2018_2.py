class Produkt:
    def senden(self):
        print('Product sent.')

    def bezahlen(self):
        print('Payment completed.')

    def verfugbarkeitPrufen(self):
        print('Product available.')

class Product:

    def __init__(self):
        self._Produkt = Produkt()

    def send(self):
        self._Produkt.senden()

    def pay(self):
        self._Produkt.bezahlen()

    def checkAvailability(self):
        self._Produkt.verfugbarkeitPrufen()

product = Product()
product.send()
product.pay()
product.checkAvailability()
    