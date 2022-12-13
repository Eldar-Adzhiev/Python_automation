import random

import pytest


@pytest.fixture(scope='function')
def function_fixture():
    return random.randint(0, 100)


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(0, 100)



@pytest.fixture(scope='session')
def session_fixture():
    return random.randint(0, 100)



def test_1(function_fixture, session_fixture):
    print(f'func fxt: {function_fixture}')
    print(f'sess fxt: {session_fixture}')


def test_2(function_fixture, session_fixture):
    print(f'func fxt: {function_fixture}')
    print(f'sess fxt: {session_fixture}')



class TestClass:

    def test_1(self, function_fixture, class_fixture, session_fixture):
        print(f'func fxt: {function_fixture}')
        print(f'class fxt: {class_fixture}')
        print(f'sess fxt: {session_fixture}')

    def test_2(self, function_fixture, class_fixture, session_fixture):
        print(f'func fxt: {function_fixture}')
        print(f'class fxt: {class_fixture}')
        print(f'sess fxt: {session_fixture}')


class TestClass1:

    def test_1(self, function_fixture, class_fixture, session_fixture):
        print(f'func fxt: {function_fixture}')
        print(f'class fxt: {class_fixture}')
        print(f'sess fxt: {session_fixture}')

    def test_2(self, function_fixture, class_fixture, session_fixture):
        print(f'func fxt: {function_fixture}')
        print(f'class fxt: {class_fixture}')
        print(f'sess fxt: {session_fixture}')
