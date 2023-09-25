########################################
#      Ф У Н К Ц И И     #
########################################

def func():
    """Documentation of func"""
    return 1
print (func.__doc__)

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(','):
        tag_list.append(tag.strip())
    
    return tag_list


split_tags('python, coursera, mooc')

#
## Аннотация типов
#
print("\nАннотация типов")

# Аргименты - int, возвращаемое значение - int
def add(x: int, y: int) -> int:
    return x + y

print(add(10, 11))
print(add('still ', 'works')) # но работает, даже если нет соответсвтия типов



#
## Именованные аргументы
#
print("\nИменованные аргументы")

def say(greeting, name):
    print('{} {}!'.format(greeting, name))
    
say('Hello', 'Kitty')
say(name='Kitty', greeting='Hello') # the same


def greeting(name='it\'s me...'): # значение name по умолчанию
    print('Hello, {}'.format(name))
    
greeting()



#
## Изменяемые аргументы
#
print("\nИзменяемые аргументы аргументы")

# В качестве аргумента функции желательно передавать неизменяемые значения immutable:
# чиловые типы, строки, кортежи, замороженные множества.
# Иначе при каждом новом вызове функции изменяемое значение будет перезаписываться и расширяться.

# Что делать с изменяемымы аргументами
def function(iterable=None):
    if iterable is None:
        iterable = []
    
# или
def function(iterable=None):
    iterable = iterable or []



#
## Функции со разным количеством аргументов
#
print("\nФункции с разным количеством аргументов")

# * для распаковки позиционных аргументов.  Позиционные – это те, которые просто подряд передаются без указания имени
# ** для распаовки именованных аргументов

def printer(*args):
    """Печатает по одному оргкменту на строке"""
    print(type(args)) # это будет кортеж tuple
    
    for argument in args:
        print(argument)

printer(1, 2, 3, 4, 5)

name_list = ['John', 'Bill', 'Amy']
printer(*name_list)  # передается как множество аргументов
printer(name_list)   # передается как один аргумент


def printer(**kwargs):
    print(type(kwargs)) # это будет словарь dict
    
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))
        
printer(a=10, b=11)

payload = {
    'user_id': 117,
    'feedback': {
        'subject': 'Registration fields',
        'message': 'There is no country for old men'
    }
}
printer(**payload)

# Можно сочетать *args и **kwags в одной функции, причем именно в этом порядке.
def megafunc(x, y, *args, **kwargs):
    print('x = {} and y = {}'.format(x, y))
    print('also args: {}'.format(args))
    print('also kwargs {}'.format(kwargs))
megafunc(10, 15, 20, 25, troll=30, dwarf=40)

# more on functions arguments
# https://docs.python.org/3/tutorial/controlflow.html#special-parameters
#
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only
#
# позиционные аргументы следуют по порядку,
# при вызове важен порядок указания аргументов


def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)     # 2
standard_arg(arg=2) # 2

pos_only_arg(1)   #1
# pos_only_arg(arg=1) TypeError: pos_only_arg() got an unexpected keyword argument 'arg'

#kwd_only_arg(3) kwd_only_arg() takes 0 positional arguments but 1 was given
kwd_only_arg(arg=3)  # 3

#combined_example(1, 2, 3) TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)          # 1 2 3 
combined_example(1, standard=2, kwd_only=3) # 1 2 3 
#combined_example(pos_only=1, standard=2, kwd_only=3)    combined_example() got an unexpected keyword argument 'pos_only'





