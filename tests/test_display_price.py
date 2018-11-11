from sale import Display, PointOfSale, DisplayMessages, Inventory, Product, \
    Money, Currency, Barcode
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


def test_barcode_contining_not_only_digits():
    display = Display()
    pos = PointOfSale(display)
    pos.onbarcode('a23')
    assert display.text() == DisplayMessages.INVALID_BARCODE.value


def test_onbarcode_not_existing_product():
    display = Display()
    i = Inventory()
    i.add_product(Product(Barcode('123'), 'book', Money(10, Currency.USD)))
    pos = PointOfSale(display, i)
    pos.onbarcode('789')
    assert display.text() == DisplayMessages.PRODUCT_NOT_FOUND.value


def test_onbarcode_existing_product():
    display = Display()
    i = Inventory()
    i.add_product(Product(Barcode('123'), 'book', Money(10, Currency.USD)))
    pos = PointOfSale(display, i)
    pos.onbarcode('123')
    assert display.text() == '10 $'
