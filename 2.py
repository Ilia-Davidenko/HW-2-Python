# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число '))
multy = 1
lst1 = []
lst2 = ()
for i in range(1, number + 1):
    multy *= i
    lst1.append(multy)
print(lst1, lst2)