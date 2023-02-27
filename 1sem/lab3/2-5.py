def search(m,e):
    if len(m) == 0:
         return 0
    i = round(len(m) / 2)
    if e == m[i]:
        return 1
    if e > m[i]:
        return search(m[i+1:],e)
    if e < m[i]:
        return search(m[:i],e)
a = int(input('Введите число\n'))
print('Введите 3 массива одинаковой длины через пробел (каждый массив на отдельной строке)')
m1 = sorted(list(map(int,input().split())))
m2 = sorted(list(map(int,input().split())))
m3 = sorted(list(map(int,input().split())))
c = search(m1,a) + search(m2,a) + search(m3,a)
print('Число найдено', c, 'раз(а)')
print("Сложность алгоритма O(3log(n))")
