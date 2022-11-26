# map - мапим функцию на последовательности
# передаем каждый элемент каждой последовательности в функцию, возвращаем результат

list1 = [7, 2, 3, 10, 12, 1]
list2 = [-1, 1, -5, 4]
list3 = [-1, 1, -5]


def multiply(x, y, z):
    return x * y * z


# передаем функцию (не результат) и списки, в количестве равном аргументам функции
res1 = map(multiply, list1, list2, list3)
print(list(res1))  # [7, 2, 75]


res2 = map(lambda x: x * 10, 'asdf')  # с помощью анонимной функции
print(list(res2))  # ['aaaaaaaaaa', 'ssssssssss', 'dddddddddd', 'ffffffffff']





# filter - фильтруем последовательность с помощью функции
# передаем каждый элемент последовательности в функцию, оставляем элемент если результат функции True
numbers = [10, 4, 2, -1, 6]


def lower_then_5(x):
    return x < 5  # убираем все что больше 5


res = filter(lower_then_5, numbers)
print(list(res))  # [4, 2, -1]


res2 = filter(lambda x: x > 5, numbers)   # с помощью анонимной функции, убираем все что меньше 5
print(list(res2))  # [10, 6]


res3 = filter(lambda s: s == 'a', 'fhdjksfhskdhfhsaadhquhwdqeq')  # убираем все буквы кроме "а"
print(list(res3))  # ['a', 'a']




# reduce - оперируем прошлым результатом функции и новым элементом последовательности
from functools import reduce


numbers = [2, 3, 4, 5, 6]  # sum 20


def add(temp_result, x):
    return temp_result + x


res1 = reduce(add, numbers)
print(res1)  # 20


# 1 итерация
# последнего результата нет, берем первый элемент 2 -> temp_result
# следующий элемент 3 -> x
# результат итерации 2 + 3 = 5

# 2 итерация
# последний результат 5 -> temp_result
# следующий элемент 4 -> x
# результат итерации 5 + 4 = 9

# 3 итерация
# последний результат 9 -> temp_result
# следующий элемент 5 -> x
# результат итерации 9 + 5 = 14

# 4 итерация
# последний результат 14 -> temp_result
# следующий элемент 6 -> x
# результат итерации 14 + 6 = 20

# итог 20

res2 = reduce(lambda temp_result, x: temp_result - x, numbers)  # с помощью анонимной функции, вычитаем все элементы
print(res2)  # -16


res3 = sum(numbers)  # эквивалент sum
print(res3)  # 20
