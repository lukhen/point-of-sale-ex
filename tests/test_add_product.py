from sale import Inventory, Barcode, Money, Product, Currency, ProductError
import pytest


def test_add_product_to_empty_inventory():
    i = Inventory()
    barcode = Barcode('123')
    price = Money(5.4, Currency.USD)
    p = Product(barcode, 'Book', price)
    assert p not in i
    i.add_product(p)
    assert p in i


def test_add_products_with_the_same_barcode():
    i = Inventory()
    p1 = Product(Barcode('234'), 'Book', Money(3.3, Currency.USD))
    p2 = Product(Barcode('234'), 'Bicycle', Money(3500, Currency.PLN))
    i.add_product(p1)
    with pytest.raises(ProductError):
        i.add_product(p2)
