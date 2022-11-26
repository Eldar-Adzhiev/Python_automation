import random


# Целые числа (int)
num = 42
num = 42_000_000  # начиная с python 3.6

type(num)
# <class 'int'>


print(num)
print(random.randint(1, 1999))


bool(0)  # False
bool(1)  # True
bool(3)  # True


6 * 6
# 36

4 ** 2
# 16

36 / 6
# 6.0

36 // 6
# 6

3 % 2  # остаток от деления 1, нечетное

4 % 2  # остаток от деления 0, четное

1 / 0
#  ZeroDivisionError: division by zero
