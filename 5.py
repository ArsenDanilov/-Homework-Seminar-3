n = int(input('Введите число: '))
i = 1
j = 0
fibonacci = 0
fibonacci_list = list()
while i < n:
    j = fibonacci
    fibonacci = i + j 
    fibonacci_list.append(fibonacci)
    i = j

fibonacci_reverse_list = fibonacci_list.copy()
print(f'{fibonacci_list}\n')

for i in range(len(fibonacci_reverse_list)):
    if i % 2 == 0:
        fibonacci_reverse_list[i] *= -1 
        

fibonacci_reverse_list.reverse()
print(fibonacci_reverse_list)

fibonacci_reverse_list.extend(fibonacci_list)

print(fibonacci_reverse_list)