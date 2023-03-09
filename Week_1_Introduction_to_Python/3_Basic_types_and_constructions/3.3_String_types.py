#-----------------------------------------------------------------------
# strings and byte strings types of variables
#-----------------------------------------------------------------------

example_string = "Курс про Python на Coursera"
print(example_string, type(example_string))

example_string = 'Курс про Python на Coursera'
print(example_string, type(example_string))

# different variations
# working versions
print("\nDouble quotes")

example_string = 'Курс про "Python" на "Coursera"'
print(example_string)

example_string = "Курс про 'Python' на 'Coursera'"
print(example_string)

## non-working versions
#example_string = "Курс про "Python" на "Coursera""
#print(example_string)

#example_string = 'Курс про 'Python' на 'Coursera''
#print(example_string)

#
# Escaping with a slash
#
print("\nEscaping with a slash")

example_string = "Курс про \"Python\" на \"Coursera\""
print(example_string)

example_string = 'Курс про \'Python\' на \'Coursera\''
print(example_string)

#
# Raw strings
#
print("\nRaw strings")

example_string = "Файл на диске c:\\\\"
print(example_string)

example_string = r"Файл на диске c:\\"
print(example_string)


#
# Spliting long string
#
print("\nSpliting long string")

example_string = "Perl — это тот язык, который одинаково " \
                 "выглядит как до, так и после RSA шифрования." \
                 "(Keith Bostic)"
print(example_string)


#
# String with the paragraphs
#
print("\nString with the paragraphs")

example_string = """
Есть всего два типа языков программирования: те, на которые 
люди всё время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)


#
# While summing and multuplying strings we got new objects
#
print("\nSumming and multuplying strings")

example_string = "Привет"
print(example_string, id(example_string)) # print adress of object

example_string += ", Мир!"
print(example_string, id(example_string))

example_string *= 3
print(example_string, id(example_string))


#
# line slices [start:stop:step]
#
print("\nline slices")

example_string = "Курс про Python на Coursera"

print(example_string[9:])
print(example_string[9:15])
print(example_string[-8:])

example_string = "0123456789"
print(example_string[::2])

example_string = "Улыбок тебе дед макаР"
print(example_string[::-1])



#
# Methods for strings
#
print("\nMethods for strings")

quote = """Болтовня ничего не стоит. Покажите мне код.

Linus Torvalds
"""
print(quote.count("о"))

print("москва".capitalize())
print("2017".isdigit())
print("3.14" in "Число Пи = 3.1415926")

example_string = "Привет"
for letter in example_string:
    print("Буква", letter)

name = ""
if not name:
    print("Имя не заполнено!")

# metod index() returns the index number of the position of the begining of substring    
first = 'Python is the language of the future.'
print(first.index('lang', 10)) # 14

#
# string formatting
#
print("\nString formatting")

# with place-holder
template = "%s — главное достоинство программиста. (%s)"
print(template % ("Лень", "Larry Wall"))

# with method format()
template = "{} не лгут, но {} пользуются формулами. ({})"
template = template.format("Цифры", "лжецы", "Robert A. Heinlein")
print(template)

# with names
template = "{num} Кб должно хватить для любых задач. ({author})"
template = template.format( num=640, author="Bill Gates" )
print(template)

# with f-strings
subject = "оптимизация"
author = "Donald Knuth"
example_string = f"Преждевременная {subject} — корень всех зол. ({author})"
print(example_string)


#
# Модификаторы форматирования
#
print("\nFormatting modifier")

num = 8
print(f"Binary: {num:#b}") # in binary
print(f"{num:.3f}")        # three decimal places


#
#Байтовые строки (bytes)
#
print("\nBytes strings")


example_bytes = b"hello"
print(example_bytes, type(example_bytes))
for element in example_bytes:
    print(element, type(element))

#error
#example_bytes = b"привет" # not ASCII
example_string = "привет"
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string, type(encoded_string))

decoded_string = encoded_string.decode()
print(decoded_string)















