my_list = [1, 2, 3, 4, 5]

# задаем генераторное выражение
gen = (x for x in my_list)

print(gen)  # generator object <genexpr>
print(type(gen))  # <class 'generator'>


# итерируемся по генератору, берущему значения списка my_list
for i in gen:
    print(i)


# преобразовываем значения на лету в каждой итерации, отдавая квадрат элемента
changing_gen = (x ** x for x in my_list)

# отсеиваем значения на лету в каждой итерации, оставляя только четные
condition_gen = (x for x in my_list if x % 2 == 0)


# list чтобы исполнить генератор и проверить результат
print(list(changing_gen))   # [1, 4, 27, 256, 3125]
print(list(condition_gen))  # [2, 4]



# генератор последовательностей, принимает начальное значение, конечное значение и шаг
r = range(0, 10, 2)

print(r)        # range(0, 10, 2)
print(type(r))  # <class 'generator'>
# исполняем генератор чтобы получить список его значений
print(list(r))  # [0, 2, 4, 6, 8]


# итерируемся по генератору, не создавая список значений, а получая каждое новое на лету
for i in range(10):
    print(i)




# генератор списков
my_list = [1, 2, 3, 4, 5]
list_gen = [x for x in my_list]  # не генератор, сразу получили готовый список

print(list_gen)  # [1, 2, 3, 4, 5]
print(type(list_gen))  # <class 'list'>

# преобразовываем значения на лету в каждой итерации, отдавая квадрат элемента, получаем готовый список
changing_list_gen = [x ** x for x in my_list]

# отсеиваем значения на лету в каждой итерации, оставляя только четные, получаем готовый список
condition_list_gen = [x for x in my_list if x % 2 == 0]

print(changing_list_gen)  # [1, 4, 27, 256, 3125]
print(condition_list_gen)  # [2, 4]






# генератор словарей
my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

# создаем новый словарь из оригинала, но только с четными ключами
dict_gen = {k: v for k, v in my_dict.items() if k % 2 == 0}
print(dict_gen)  # {2: 2, 4: 4}




# создаем новый список из ключей словаря, возведенных в квадрат
list_gen = [k * k for k in my_dict.keys()]
print(list_gen)  # [1, 4, 9, 16, 25]



# создаем словарь с ключами из 1 списка и значенями из другого
keys = [1, 2, 3, 4, 5, 1]
values = [11, 12, 13, 14, 15]

# zip совмещает 2 последовательности в список из tuple
print(list(zip(keys, values)))  # [(1, 11), (2, 12), (3, 13), (4, 14), (5, 15)]

# генерируем новый словарь из совмещенных элементов 2х списков
di = {k: v for k, v in zip(keys, values)}
print(di)  # {1: 11, 2: 12, 3: 13, 4: 14, 5: 15}
