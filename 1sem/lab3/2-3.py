def factorial(n):
    if n == 0:
        return 1
    for i in range(n):
        num = n * factorial(n-1)
    return num
n = int(input('Введите n\n'))
f = factorial(n)
print('n! =',f)
print("Сложность алгоритма O(n!)")
