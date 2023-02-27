print("Введите ваш массив через пробел")
arr = list(map(int, input().split()))

for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

print("Сложность алгоритма пузырьковой сортировки O(n^2)")

import timeit

code_to_test_1 = """
from random import randint
N = 100
arr = []
for i in range(N):
    arr.append(randint(1, 999))

for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
"""
code_to_test_2 = """
from random import randint
N = 100
arr = []
for i in range(N):
    arr.append(randint(1, 999))
arr.sort()
"""

elapsed_time_1 = timeit.timeit(code_to_test_1, number=100) / 100
print("Время выполнения пузырьковой сортировки", elapsed_time_1)
elapsed_time_2 = timeit.timeit(code_to_test_2, number=100) / 100
print("Время выполнения метода sort()", elapsed_time_2)

if elapsed_time_1 > elapsed_time_2:
    print("Метод sort() быстрее пузырьковой сортировки")
else:
    print("Пузырьковая сортировка быстрее метода sort()")
