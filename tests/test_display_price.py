from sale import Display, PointOfSale, DisplayMessages
import pytest


def test_barcode_is_empty_string():
    display = Display()
    pos = PointOfSale(display)
    pos.onbarcode('')
    assert display.text() == DisplayMessages.INVALID_BARCODE.value


def test_Inventory_is_empty():
    display = Display()
    pos = PointOfSale(display)
    pos.onbarcode('123')
    assert display.text() == DisplayMessages.PRODUCT_NOT_FOUND.value


@pytest.mark.skip(reason="wait until Barcode class is implemented and tested")
def test_barcode_contining_not_only_digits():
    display = Display()
    pos = PointOfSale(display)
    pos.onbarcode('a23')
    assert display.text() == DisplayMessages.INVALID_BARCODE.value
