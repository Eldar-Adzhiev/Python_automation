empty_tuple = ()
empty_tuple1 = tuple()


tpl = tuple([1, 2, 3, 4, 5])
tpl1 = tuple('1234567')

tpl[0]  # 1
tpl[::-1]  # (5, 4, 3, 2 ,1)


tpl[1] = 2  # ValueError, не можем менять кортеж


bool(())  # False
bool((1, 2, 3))  # True
