import os
import random

import pytest


@pytest.fixture(scope='session')
def random_func():
    return random.randint(0, 100)


@pytest.fixture(autouse=True, scope='function')
def new_file(random_func):
    file_name = f'my_file_{random_func}'
    f = open(file_name, 'w')
    f.write('32178361263126378126387126873126736127836718263781263876123')
    f.flush()

    # breakpoint()

    yield f

    f.close()
    os.remove(file_name)



def test(new_file):
    pass


def test1():
    pass


def test2():
    pass