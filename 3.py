import random

list_1 = [round(random.uniform(0, 10), 1) for i in range (4)]
print()
print(f'Вывод первоначального списка вещественных чисел: {list_1}\n')

list_2 = list()

for i in range (len(list_1)):
    list_2.append(round((list_1[i] % 1), 1))

print(f'Вывод списка, состоящего из дробных частей элементов первоначального списка: {list_2}\n')
print(f'Максимальное и минимальное дробные значения элементов первоначального массива равны: {max(list_2)} и {min(list_2)}\n')

difference = round(max(list_2) - min(list_2), 1)
print(f'Разница максимальной и минимальной дробных частей равна: {difference}')




