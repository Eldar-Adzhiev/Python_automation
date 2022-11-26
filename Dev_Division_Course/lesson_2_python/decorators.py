from functools import wraps

counter = {}  # счетчик в виде словаря, чтобы хранить имя функции и количество ее вызовов


def count_decorator(f):  # функция, принимает на вход функцию

    @wraps(f)  # не позволяет меняться имени декорируемой функции и ее doc-string
    # вложенная функция
    # принимает любые позиционные и именованные аргументы переданные от вызова оригинала
    def wrapper(*args, **kwargs):
        name = f.__name__  # у декорируемой функции можно получить название

        if name in counter:
            # если счетчик такой функции уже есть - добавим +1 вызов
            counter[name] += 1

        else:
            # если счетчика такой функции нет - определим первый вызов
            counter[name] = 1

        return f(*args, **kwargs)  # вызовем оригинал с аргументами оригинала и вернем результат

    return wrapper    # возвращает вложенную функцию


@count_decorator  # "навешиваем" декоратор на функцию, будет вызываться автоматически при каждом вызове func
def func(x, y=6):
    """test"""
    return x * y


print(func.__name__)  # без @wraps в декораторе вернет wrapper


@count_decorator  # "навешиваем" декоратор на функцию, будет вызываться автоматически при каждом вызове func1
def func1(x, y):
    """test"""
    return x * y


print(func1.__name__)  # без @wraps в декораторе вернет wrapper


# не декорируем, не участвует в подсчете вызовов
def func2(x):
    print(x)


print(func2.__name__)  # func2


r1 = func(1, 2)
r2 = func(2, y=3)
r3 = func(3)

r4 = func1(1, 1)


print(r1, r2, r3, r4)  # 2 6 18 1
print(counter)  # {'func': 3, 'func1': 1}
