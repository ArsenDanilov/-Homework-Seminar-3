from random import randint

list_1 = [randint(0, 10) for i in range (10)]
print(f'Вывод первоначального списка: {list_1}')


list_2 = list()

print()

for i in range (int(len(list_1) / 2)):
    n = list_1[i] * list_1[-i - 1]
    list_2.append(n)
    n = 0

print(f'Вывод нового списка, состоящего из произведений пар чисел: {list_2}')