import pytest


@pytest.fixture
def _fly():
    print("prepare")
    yield 49
    print("shutdown")
