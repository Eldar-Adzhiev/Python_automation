import random
import time

import pytest


@pytest.mark.parametrize('i', list(range(10)))
def test_even(i):
    time.sleep(1)
    assert i % 2 == 0



di = {1: 1, 2: 2, 3: 4}

@pytest.mark.parametrize('k, v', di.items())
def test_dict(k, v):
    assert k == v



@pytest.fixture(params=list(range(10)))
def random_func(request):
    res = request.param
    print(res)
    yield res
    print(res * 10)


def test_random(random_func):
    pass


