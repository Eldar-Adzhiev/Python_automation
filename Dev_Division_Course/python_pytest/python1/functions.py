def add(x, y):  # x, y - аргументы функции
    sm = x + y
    print(sm)
    return sm  # возвращаем значение тому, кто вызвал функцию


res1 = add(1, 3)
res2 = add(2, 5)
res3 = add(1, 9)

print(res1, res2, res3)
print(type(add))
# <class 'function'>


# создаем свое исключение
class MyException(Exception):
    pass


def division(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        raise MyException()

try:
    division(2, 0)
except MyException:
    print('все хорошо, наше собственное исключение перехвачено')



