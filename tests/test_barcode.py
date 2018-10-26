from sale import Barcode, InvalidBarcodeError
import pytest


def test_empty_barcode():
    with pytest.raises(InvalidBarcodeError):
        Barcode('')
