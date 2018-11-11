from enum import Enum
import re


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return other._currency == self._currency and self._amount == other._amount


class Currency(Enum):
    USD = '$'
    PLN = 'zł'


class Barcode:
    def __init__(self, barcode_string):
        barcode_string = str.strip(barcode_string)

        if re.match('^\\d+$', barcode_string) is None:
            raise InvalidBarcodeError('Barcode string cannot be empty.')
        self._barcode_string = barcode_string

    def __eq__(self, other):
        if isinstance(other, Barcode) and \
           other._barcode_string == self._barcode_string:
            return True

    def __hash__(self):
        return hash(self._barcode_string)


class InvalidBarcodeError(Exception):
    pass


class ProductError(Exception):
    pass


class Display:
    def __init__(self):
        self._text = ''

    def text(self):
        return self._text

    def print_message(self, message):
        self._text = message


class Inventory:
    def __init__(self):
        self._dict_of_products = {}

    def __len__(self):
        return 0

    def __contains__(self, product):
        return product.barcode in self._dict_of_products.keys()

    def add_product(self, product):

        self._dict_of_products[product.barcode] = product

    def get_product_by_barcode(self, barcode):
        return self._dict_of_products.get(barcode, None)


class Product:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price


class PointOfSale:
    def __init__(self, display, inventory=Inventory()):
        self._display = display
        self._inventory = inventory

    def onbarcode(self, barcode):
        try:
            barcode = Barcode(barcode)
            if len(self._inventory) == 0:
                self._display.print_message(
                    DisplayMessages.PRODUCT_NOT_FOUND.value)

        except InvalidBarcodeError:
            self._display.print_message(
                DisplayMessages.INVALID_BARCODE.value)


class DisplayMessages(Enum):
    INVALID_BARCODE = 'Invalid barcode'
    PRODUCT_NOT_FOUND = 'Product not found'
