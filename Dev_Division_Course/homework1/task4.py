some_list = [1, 4, 6, 9, 2, 3, 5]


def reverse_1(lst):
    return lst[::-1]


def reverse_2(lst):
    lst.reverse()
    return lst


def reverse_3(lst):
    return list(reversed(lst))


def reverse_4(lst):
    result = []
    for i in lst:
        result.insert(0, i)  # забираем элемент с конца, вставляем в начало нового списка
    return result


def reverse_5(lst):
    for i in range(len(lst)):
        lst.insert(i, lst.pop())  # забираем элемент с конца, вставляем в начало текущего
    return print()


def reverse_6(lst):
    for i in range(len(lst) // 2):  # проходим по половине длины списка
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]  # меням симметричные индексы местами
    return lst


def reverse_7(lst):
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]
