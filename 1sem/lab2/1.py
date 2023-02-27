def search(m,e,c):
    if len(m) == 0:
         return -1
    i=round(len(m)/2)
    if e == m[i]:
        return c
    if e > m[i]:
        return search(m[i+1:],e,c+1)
    if e < m[i]:
        return search(m[:i],e,c+1)
a = sorted(map(float,input('Введите элементы массива через пробел\n').split()))
b = float(input('Введите число, которое нужно найти\n'))
res = search(a,b,1)
if res == -1:
    print('Такого элемента нету в данном массиве')
else:
    print(res)
