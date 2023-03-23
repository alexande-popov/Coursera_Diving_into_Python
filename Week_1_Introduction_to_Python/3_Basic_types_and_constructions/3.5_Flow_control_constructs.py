#-----------------------------------------------------------------------
# Конструкции управления потоком
#-----------------------------------------------------------------------

#
# if-elif-else
#
print("\nif-elif-else")

company = "google.com"

if "my" in company:
    print("Подстрока my найдена")
elif "google" in company:
    print("Подстрока google найдена")
else:
    print("Подстрока не найдена")


#
score_1 = 5
score_2 = 0
winner = "Argentina" if score_1 > score_2  else "Jamaica"
print(winner)


#
# Loops
#
print("\nLoops")

# from 0 to ...
for i in range(3):
    print(i)
    
print("\n")
for i in range(5, 8):
    print(i)

# not work
print("\n")
for i in range(8, 5):
    print(i)

# with step
print("\n")
for i in range(1, 10, 2):
    print(i)

# inversted
print("\n")
for i in range(10, 5, -1):
    print(i)


#
# pass, break, continue
#
print("\npass, break, continue")

# pass - пустой блок, ничего не делает
print("\n")
for i in range(100):
    pass

# break - выход из цикла досрочно
print("\n")
result = 0
while True:
    result += 1
    if result >= 100:
        break
print(result)

#
print("\n")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - переод к следующей итерации цикла
# без выполнения оставшихся инструкций в блоке
print("\n")
result = 0
for i in range(10):
    if i % 2 != 0:
        continue
    result += i
print(result)









