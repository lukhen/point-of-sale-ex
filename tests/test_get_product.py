from sale import Inventory, Barcode, Product, Money, Currency


def test_get_product_from_empty_inventory():
    i = Inventory()
    b = Barcode('123')
    assert i.get_product_by_barcode(b) is None


def test_get_product_when_it_exists():
    i = Inventory()
    p = Product(Barcode('123'), 'book', Money(10, Currency.USD))
    i.add_product(p)
    retrieved = i.get_product_by_barcode(Barcode('123'))
    assert retrieved is not None
    assert retrieved.name == p.name
    assert retrieved.price == p.price


def test_get_not_existing_product_from_unempty_inventory():
    i = Inventory()
    p = Product(Barcode('123'), 'book', Money(10, Currency.USD))
    i.add_product(p)
    assert i.get_product_by_barcode(Barcode('234562')) is None
