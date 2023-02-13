from random import randint

list_1 = [randint(0, 10) for i in range (10)]
print(list_1)

summa = 0
for i in range (len(list_1)):
    if i % 2 != 0:
        summa += list_1[i]
        print(f'{summa} = {summa} + {list_1[i]} = {summa + list_1[i]}')

print()
print()
print(summa)

