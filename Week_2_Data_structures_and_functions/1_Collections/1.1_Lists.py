empty_list = []
empty_list = list()

none_list = [None] * 10

collections = ['list', 'tuple', 'dict', 'set']
print(len(collections))

user_data = [
    ['Elena', 4.4],
    ['Andrey', 4.2]
]

print(collections)
print(collections[0])
print(collections[-1])

print(user_data)
print(user_data[0])
print(user_data[1][1])

collections[3] = 'frozenset'
print(collections)

#
## Поиск элементов
#
print("\nПоиск элементов")

# Проверить, содержит ли список некоторый объект,
# можно с помощью ключевого слова "in"
"tuple" in collections

# метов index() выдает номер позиции, на которой встречается указанный элемент
myList = ['1', '11', 1, 'a', 'x', 1.1]
el1 = myList.index(1) # 2
elx = myList.index('x') # 4
print(myList)
print(el1)
print(elx)

#
## Срезы в списках
#
print("\nСрезы в списках")

range_list = list(range(10))
print(range_list)

# [fist:last:step]
range_list[1:3]
range_list[3:]
range_list[:5]
range_list[::2]
range_list[::-1]
range_list[1::2]
range_list[5:1:-1]

# срез списка -- это новый объект
range_list[:] is range_list



#
## Итерации по спискам
#
print("\nИтерации по спискам")

collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}'.format(collection))

# Часто бывает нужно получить индекс текущего элемента при итерации.
# Для этого можно использовать встроенную функцию enumerate
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

# enumerate позволяет задавать номер счетчика, с которого начинается.
# позволяет делать нумерованные списки
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, start = 3))
print(counter_list)
# Output: [(3, 'apple'), (4, 'banana'), (5, 'grapes'), (6, 'pear')]


#
## Добавление и удаление элементов
#
print("\nДобавление и удаление элементов")

# append -- добавляет один элемент
# extend -- расширяет списком

collections.append('OrderedDict')
print(collections) # ['list', 'tuple', 'dict', 'set', 'OrderedDict']

collections.extend(['ponyset', 'unicorndict'])
print(collections) # ['list', 'tuple', 'dict', 'set', 'OrderedDict', 'ponyset', 'unicorndict']

del collections[4]
del collections[4]
del collections[-1]
print(collections) # ['list', 'tuple', 'dict', 'set']

collections.extend('set')
print(collections) # ['list', 'tuple', 'dict', 'set', 's', 'e', 't']

collections += [None]
collections += ['a1', 'a2']
print(collections) # ['list', 'tuple', 'dict', 'set', 's', 'e', 't', None, 'a1', 'a2']
del collections[len(collections):3:-1] # del до 3+1 элемента
print(collections) # ['list', 'tuple', 'dict', 'set']

# insert()
collections.insert(1, "set") # вставить на 1+1 место элемент "set" 
print(collections) # ['list', 'set', 'tuple', 'dict', 'set']
collections.remove("set")  # удаляет первый попавшися
print(collections) # ['list', 'tuple', 'dict', 'set']

# pop()
last_el = collections.pop()   # удаляет и возвращает последний элемент
print(last_el, collections)
first_el = collections.pop(0) # удаляет и возвращает первый элемент
print(first_el, collections)

#
## List как стек
#
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
del stack[-1]

#
## list как очередь queues (FIFO - first in, first out)
#
# Добавлять и удалять с конца списка - быстрая операция для list
# Добавлять и удалять с начала списка - медленная операция для list
# Для очередей специально есть collections.deque, которая быстрая
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival



#
## min, max, sum, count
#
print("\nmin, max, sum, count")

numbers = [4, 17, 19, 9, 2, 6, 10, 13, 4, 4]

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers.count(4)) # число входов элемента 4


#
## Преобразование списка в строку методом join()
#
print("\nПреобразование списка в строку")
tag_list = ['python', 'course', 'coursera']
# или
str.join(', ', tag_list)
print(', '.join(tag_list))


#
## Сортировка
#
print("\nСортировка")


import random

numbers = []
for _ in range(10): # название переменной не интересно, оно не используется
    numbers.append(random.randint(1, 20))
    
print(numbers)
print(sorted(numbers)) # создается новое место в памяти
print(numbers)

numbers.sort() # записывает в исходный список
print(numbers)

# в обратном порядке
print(sorted(numbers, reverse=True))

numbers.sort(reverse=True)
print(numbers)

print(reversed(numbers))
print(list(reversed(numbers)))
# reversed() работает с произвольными последовательностями или с
# объектами с __reversed__() методом и всегда возвращает итератор,
# обходя который можно получить элементы входной последовательности
# в обратном порядке.

# Сортировка строковых объектов
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')      # 2
fruits.count('tangerine')  # 0
fruits.index('banana')     # 3
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.append('grape')
fruits.sort()  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()   # 'pear'



#
## Методы составления и изменение списков
#
print("\nМетоды составления и изменения списков")

##
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# эквиввалентно
squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]


## с условиями
combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)

# эквиввалентно
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

##
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]  # [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]  # [0, 2, 4]

# apply a function to all the elements
[abs(x) for x in vec]  # [4, 2, 0, 2, 4]

















