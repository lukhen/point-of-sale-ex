from sale import Barcode, InvalidBarcodeError
import pytest


def test_empty_barcode():
    with pytest.raises(InvalidBarcodeError):
        Barcode('')


@pytest.mark.skip(reason='Skip until Barcode.__eq__ is implemented and tested')
def test_barcode_ends_with_carriage_return():
    assert Barcode('123\n') == Barcode('123')


def test_barcode_equal():
    assert Barcode('123') == Barcode('123')
    assert Barcode('123') != Barcode('124')
