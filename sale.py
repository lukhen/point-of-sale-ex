from enum import Enum


class Display:
    def text(self):
        return DisplayMessages.INVALID_BARCODE.value


class PointOfSale:
    def __init__(self, display):
        pass

    def onbarcode(self, barcode):
        pass


class DisplayMessages(Enum):
    INVALID_BARCODE = 'Invalid barcode'
