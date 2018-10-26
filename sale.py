from enum import Enum


class Display:
    def __init__(self):
        self._text = ''

    def text(self):
        return self._text

    def print_message(self, message):
        self._text = message


class Inventory:
    def __len__(self):
        return 0


class PointOfSale:
    def __init__(self, display, inventory=Inventory()):
        self._display = display
        self._inventory = inventory

    def onbarcode(self, barcode):
        if barcode == '':
            self._display.print_message(
                DisplayMessages.INVALID_BARCODE.value)

        elif len(self._inventory) == 0:
            self._display.print_message(
                DisplayMessages.PRODUCT_NOT_FOUND.value)


class DisplayMessages(Enum):
    INVALID_BARCODE = 'Invalid barcode'
    PRODUCT_NOT_FOUND = 'Product not found'
