import random

import pytest


@pytest.fixture()
def random_value():
    print('Entering! Before Test!')
    res = random.randint(0, 100)
    yield res
    print('Exiting! After Test!')




def test_1(random_value):
    print('INSIDE TEST1!!!')
    assert random_value > 50


def test_2(random_value):
    print('INSIDE TEST2!!!')
    assert random_value > 50

