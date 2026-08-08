from main import ClassUnderTesting
import pytest


def test__getattribute__if_statement():
    """
    the __getattribute__ in the class ClassUnderTesting is overriden and has the if == 'year_made'
    statement that returns 1976 specifically for the 'year_made' attribute
    """
    a = ClassUnderTesting()
    assert a.year_made == 1976


def test__getattr__fallback():
    """
    the __getattr__ method is a fallback method for the __getattribute__ method
    and only returns value for the 'justice' attribute and raises AttributeError
    otherwise
    """
    a = ClassUnderTesting()
    assert a.justice == 7778


def test_fly(_fly):
    """
    _fly value is identified in the 'conftest.py' file and is available in
    pytests without importing
    """
    assert _fly == 49, "flying over the rainbow"


def test_fly_sum(_fly):
    print(_fly)
    assert _fly + 1 == 50, "flying over the rainbow 2"


def test_approxx():
    assert 1 == pytest.approx(0.9999999)


@pytest.mark.parametrize("a, b, result", [(1, 2, 3), (78, 2, 80)])
def test_summation(a, b, result):
    assert a + b == result


def test_default_descriptor_value_before_set():
    """
    ClassUnderTesting class has a descriptor defined and returns the _hidden_value
    of the instance. However if the _hidden_value was not set with __set__ method
    it returns a default string
    """
    a = ClassUnderTesting()
    assert a.my_descriptor == "This is the default value of the descriptor"


def test_descriptor_value_after_set():
    a = ClassUnderTesting()
    a.my_descriptor = "new value"
    assert a.my_descriptor == "new value"
