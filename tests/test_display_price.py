from sale import Display, PointOfSale


def test_barcode_is_empty_string():
    display = Display()
    pos = PointOfSale(display)
    pos.onbarcode('')
    assert display.text() == 'Invalid barcode'
