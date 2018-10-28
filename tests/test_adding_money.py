from sale import Money


def test_equalisty_money_with_the_same_currency():
    assert Money(1, '$') == Money(1, '$')
    assert Money(1, '$') != Money(2, '$')
