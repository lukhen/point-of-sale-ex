from sale import Display, PointOfSale, DisplayMessages


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
