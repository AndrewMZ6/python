from test1 import A
import pytest


def test_proble():
    a = A()
    assert a.flare == 46
    assert a.justice == 7778


def test_fly(_fly):
    assert _fly == 49, "flying over the rainbow"


def test_fly_sum(_fly):
    print(_fly)
    assert _fly + 1 == 50, "flying over the rainbow 2"


def test_approxx():
    assert 1 == pytest.approx(0.9999999)


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (78, 2, 80)])
def test_summation(a, b, result):
    assert a + b == result
