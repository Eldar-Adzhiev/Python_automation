# обычная функция сложения

def add(x, y):
    return x + y


r1 = add(1, 10)  # сложим числа, получим 11
print(r1)

r2 = add('abc', 'def')  # сложим строки, получим abcdef
print(r2)



def func():
    print('hello')
    # функция ничего не возвращает, только печатает hello


func()
func()

print(func())  # None, так как нет return




# работа с позиционными и именованными аргументами
def func(a, b, c=2):
    return a + b + c


r1 = func(1, 2)  # a -> 1, b -> 2, c -> 2 (по умолчанию)
print(r1)  # 5

r2 = func(1, 2, 3)    # a -> 1, b -> 2, c -> 3
print(r2)  # 6

r3 = func(1, b=5, c=6)    # a -> 1, b -> 2, c -> 2 (по умолчанию)
print(r3)  # 12

# передали "а" и позиционно и именованно -> ошибка
# r4 = func(6, a=3)
# print(r4)

# передали "b" и позиционно и именованно -> ошибка
# r5 = func(1, 2, b=6)
# print(r5)





# любое количество позиционных аргументов
def func(*args):
    return args


r1 = func(1, 2, 3, 'abc', 'dsadsada', '1111')
print(r1)  # (1, 2, 3, 'abc', 'dsadsada', '1111')

r2 = func()
print(r2)  # () - пустое количество аргументов

r3 = func(1)
print(r3)  # (1,) - 1 аргумент в tuple




# любое количество именованных аргументов
def func(**kwargs):
    return kwargs


r1 = func(a=1, b=2, c=3)
print(r1)  # {'a': 1, 'b': 2, 'c': 3}

r2 = func()
print(r2)  # {} - пустое количество аргументов

r3 = func(a='python')
print(r3)  # {'a': 'python'} - 1 аргумент в словаре



# любое количество и позиционных и именованных аргументов
def func(*args, **kwargs):
    return args, kwargs


r1 = func(1, 2, 3, 'abc', a=4, b=5, c=6)
print(r1)  # ((1, 2, 3, 'abc'), {'a': 4, 'b': 5, 'c': 6})

pos_args, named_args = func(1, 2, 3, 'abc', a=4, b=5, c=6)

print(pos_args)    # (1, 2, 3, 'abc')
print(named_args)  # {'a': 4, 'b': 5, 'c': 6}




# проставление результата 1 функции в вход 2 функции
def func_a(x, y):
    return x + y


def func_b(x, y):
    return x + y


# сначала высчитывается func_b(1, 2)
# потом высчитывается func_b(3, 4)

# результаты подставятся в func_a(3, 7)
res = func_a(func_b(1, 2), func_b(3, 4))
print(res)  # 10



# анонимная функция без названия
f = lambda x, y: x + y
res = f(1, 10)  # 11

res2 = (lambda x, y: x + y)(1, 10)  # сразу вызываем, без присваивания функции в переменную
print(res2)  # 11
