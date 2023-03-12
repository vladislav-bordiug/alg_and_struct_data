from random import randint,uniform
#функция хэширования, которая создает словарь типа ключ: индекс
def hash(M,mas,C):
    h = {}
    for i in mas:
        #индекс элемента в хэш-таблице вычисляем по выражению M*((K*C)mod1)
        index = int(M*((i*C)%1))
        #добавляем в словарь
        h[i] = index
    return h
M = int(input('Введите длину массива\n'))
mas = list(map(int,input('Введите ключ(и) через пробел\n').split()))
#генерируется рандомное C в интервале от 0 до 1
C = uniform(0,1)
print('C:',C)
print('Значения хэш-функции для введенных ключей:')
#вызывает функцию хэширования, передавая туда длину массива, ключи и C
h = hash(M,mas,C)
#выводим значение хэш-функции для каждого ключа
for a in h:
    print('h(',a,') = ',h[a],sep='')
