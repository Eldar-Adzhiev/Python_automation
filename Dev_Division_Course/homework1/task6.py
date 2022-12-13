import gc

my_str = '0409128473242875610432423...'  # 1Gb из 1.2Gb


# считаем каждую цифру
count_0 = my_str.count('0')
count_1 = my_str.count('1')
count_2 = my_str.count('2')
# ....


# удаляем оригинал
del my_str
gc.collect()


# передаем счетчик и значение в format padding (конструкция :^), который создает и соединяет куски строк в cPython,
# возвращая в Python готовую цельную строку без выделения необходимой памяти
my_str = f'{0:0^{count_0}}{1:1^{count_1}}{2:2^{count_2}}'


print(my_str)  # prints '0000000111111222222....'
