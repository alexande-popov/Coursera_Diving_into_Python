###################################
###   S E T    ( Н А Б О Р )    ###
###################################

"""
Set - это неупорядоченная коллекция без повторяющихся элементов.
Основное использование включает тестирование членства и
устранение повторяющихся записей.
Set-объекты также поддерживают математические операции:
объединение, пересечение, разность и симметричную разность

Фигурные скобки {} или функция set() могут использоваться для создания наборов.
Примечание: чтобы создать пустой набор, вы должны использовать
set(), а не {}; последний создает пустой словарь

Хэшируются, состоят из неизменяемых объектов. Но сами изменяются.

Бывают frozenset: они хешируются и сами неизменяемые.
"""


#
## Задание множеств
#
print("\nЗадание множеств")

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)           # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}

number_set = {1, 2, 3, 4, 5}
2 in number_set  # True
number_set.add(6)
number_set.add(6)
number_set.remove(1)

a = set('abracadabra')
b = set('alacazam')
print("a:", a)
print("b:", b)
print("a-b:", a-b, "разность")    # в a, но не в b
print("a|b:", a|b, "объединение")
print("a&b:", a&b, "пересечение")
print("a^b:", a^b, "симметрическая разность") # в a или b, но не в обоих

"""
Есть функции для математических операций с множествами
union(),
intersection(),
difference(), 
symmetric_difference(),
issubset(),
issuperset()
"""
