print("Введите массив чисел через пробел")
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] += 3
for i in range(len(arr)):
    arr[i] *= -1
for i in range(len(arr)):
    arr[i] += 100
print(arr)

print("Сложность алгоритма O(3n)")
