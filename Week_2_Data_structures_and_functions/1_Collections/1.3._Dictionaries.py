########################################
#      СЛОВАРЬ   ( D I C T  )     #
########################################

# Словари предоставляю быстрый доступ по ключу (за констатное время),
# за счет хэширования к объектам словаря.
# Ключи не изменяемы (хэшируются, сворачиваются) - immutable objects (целые числа, None, строки, кортежи).
# Объекты словаря изменяются - mutable objects. 


#
## Задание словаря.
#
print("\nЗадание словаря")

empty_dict = ()
empty_dict = dict()

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
a == b == c == d == e == f  # True

g = {x: x**2 for x in (2, 4, 6)}  # {2: 4, 4: 16, 6: 36}


#
## Методы со словаряем.
#
print("\nМетоды со словарем")

d = dict([('two', 2), ('one', 1), ('three', 3)])

# Обращение к элементам словаря. 2
d['two']

# Попытка угадать по ключу
d.get('two', 'not found') # 2
d.get('aaa', 'not found') # 'not found'
'two' in d                # True

# Лист всех ключей ['two', 'one', 'three']
list(d)

# Число элементов в словаре 3
len(d)

# Установить новое значение для элемента
d['two'] = 5

#
del d['two']

# если нет такого ключа, то добаваить, если есть, то ничего не делать
d.setdefault('two', 2)   # 3
d.setdefault('two', 77)  # 3

# итератор по ключам. аналогично iter(d.keys())
iter(d)

# Предстваление словаря в виде пар (key, value)
d.items()   # dict_items([('two', 2), ('one', 1), ('three', 3)])

# Представление ключей
d.keys()    # dict_keys(['two', 'one', 'three'])

# Представление значений
d.values()  # dict_values([2, 1, 3])

# Удаление и возвращение значение элемента
d.pop("three")               # 3
d.pop("four", "there is no") # 'there is no'

# Удаление последнего и возвращение пары (key, value)
d['three'] = 3
d.popitem()               # ('three', 3)

# Добавить новое значение для элемента
d['ten'] = 10

#
## Итерации по словарю
#
print("\nИтерации")

d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)

for key in d:
    print(key)

# the same
for key in d.keys():
    print(key)

for val in d.values():
    print(val)

for key, val in d.items():
    print(key, val)





#
## Упорядоченные словари OrderedDict
#
print("\nOrderedDict-упорядоченнвые словари")

from collections import OrderedDict

ordered = OrderedDict()

for num in range(10):
    ordered[num] = str(num)

for key in ordered:
    print(key)






















