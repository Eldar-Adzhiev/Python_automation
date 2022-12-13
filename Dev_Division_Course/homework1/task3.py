my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
my_dict1 = {'a': 50111110, 'b': 5874, 'c': 560, 'd': 40222220, 'e': 5874, 'f': 2111110}

def dict_max_keys(d, max_keys):
    return sorted(d, key=d.get)[-max_keys:]  # сортируем ключи по их значениям, берем старшие два


print(dict_max_keys(my_dict, 3))
print(dict_max_keys(my_dict1, 2))
