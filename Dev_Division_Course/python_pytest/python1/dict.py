empty_dict = {}
empty_dict1 = dict()


empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
empty_dict['key2'] = 'value344555'  # перезапишем прошлое значение


empty_dict.update({'key3': 'value3'})
empty_dict['key3']  # value3

empty_dict['key4']  # KeyError - нет такого ключа
empty_dict.get('key4', 'No such key')  # метод get позволяет задать значение по умолчанию, если ключ отсутствует


del empty_dict['key3']  # удаляем ключ

'key1' in empty_dict  # вхождение по ключам

bool({})  # False
bool({1: 1})  # True


# Работа со словарями
for k in empty_dict:
    print(k)  # итерируемся по ключам словаря

for k, v in empty_dict.items():
    print(k, v)  # итерируемся по кортежам (k, v)

for v in empty_dict.values():
    print(v)  # итерируемся по значениям словаря


# порядок добавления ключей сохраняется
d = {2: 0, 3: 0, 1: 0, 5: 0, 4: 0}
# d
# >>> {2: 0, 3: 0, 1: 0, 5: 0, 4: 0}


# итерируемся по отсортированным ключам
for k in sorted(d):
    print(d[k])  # печатаем значение ключа на каждой итерации
