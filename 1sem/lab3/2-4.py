print("Введите массив чисел через пробел")
m = list(map(int, input().split()))
for i in range(len(m)):
    for j in range(len(m)):
        for z in range(len(m)):
            m[z] = m[i] + m[j]
print(m)
print("Сложность алгоритма O(n^3)")
