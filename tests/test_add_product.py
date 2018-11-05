from sale import Inventory, Barcode, Money, Product, Currency
import pytest


def test_add_product_to_empty_inventory():
    i = Inventory()
    barcode = Barcode('123')
    price = Money(5.4, Currency.USD)
    p = Product(barcode, 'Book', price)
    assert p not in i
    i.add_product(p)
    assert p in i
