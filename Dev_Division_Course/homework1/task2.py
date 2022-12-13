def print_sum(n):
    summa = 0
    while n != 0:
        summa = summa + n % 10  # остаток от деления прибавляем в общей сумме
        n = n // 10  # отрываем последний порядок

    print(summa)
    return summa


print_sum(1234567890)  # prints 45



def print_sum(n):
    summa = sum(map(int, str(n)))  # мапим строковое представление числа на int и получаем сумму этого списка

    # from functools import reduce
    # summa = reduce(lambda x, y: int(x) + int(y), str(n))

    print(summa)
    return summa


print_sum(1234567890)  # prints 45
