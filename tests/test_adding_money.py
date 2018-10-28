from sale import Money, Currency


def test_equalisty_money_with_the_same_currency():
    assert Money(1, Currency.USD) == Money(1, Currency.USD)
    assert Money(1, Currency.USD) != Money(2, Currency.USD)
