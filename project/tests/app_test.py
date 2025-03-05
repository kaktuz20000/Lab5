from src.functional import calculate


def test_calculate():
    assert calculate(2, 3) == 5
    assert calculate(-1, 1) == 0
