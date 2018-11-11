from sale import Inventory, Barcode


def test_get_product_from_empty_inventory():
    i = Inventory()
    b = Barcode('123')
    assert i.get_product_by_barcode(b) is None
