import sort
import timeit

code_to_test_1 = """
import sort
from random import randint
arr = []
N = 100
for i in range(N):
    arr += [randint(1, 999)]
sort.quick(arr)
"""
code_to_test_2 = """
import sort
from random import randint
arr = []
N = 100
for i in range(N):
    arr += [randint(1, 999)]
sort.rascheska(arr)
"""

time_1 = timeit.timeit(code_to_test_1, number=100) / 100
print("Время выполнения быстрой сортировки", time_1)
time_2 = timeit.timeit(code_to_test_2, number=100) / 100
print("Время выполнения сортировки расческой", time_2)

b = list(map(float,input('Введите элементы массива через пробел\n').split()))
print('Введите номер алгоритма сортировки, который вы хотите использовать: 1 (быстрая сортировка) или 2 (сортировка раческой)')
c = int(input())
if c == 1:
    print(sort.quick(b))
else:
    print(sort.rascheska(b))
