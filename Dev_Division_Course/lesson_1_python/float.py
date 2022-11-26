from decimal import Decimal


float_num = 3.74
float_num1 = 3.14e2  # 3.14 * 100


print(type(float_num))
# <class ‘float’>

print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)  # 0.9999999999
#  0.1 -> 0.10000000001


precise_float = Decimal('0.111111111111')
print(precise_float)

# конвертация
print(float(int(float_num)))


bool(0.0)  # False
bool(0.5)  # True
