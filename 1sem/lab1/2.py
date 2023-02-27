def transp(m2):
    i = len(m2)
    j = len(m2[0])
    m = [0]*j
    for k in range(j):
        m[k] = [0]*i
    for k in range(j):
        for l in range(i):
            m[k][l]=m2[l][k]
    return(m)
def proizv(m1,m2):
    i = len(m1)
    j = len(m2[0])
    m = [0]*i
    for k in range(i):
        m[k] = [0]*j
    for k in range(i):
        for l in range(j):
            for x in range(len(m2)):
                m[k][l]+=m1[k][x]*m2[x][l]
    return(m)
m = []
m2 = []
h = int(input('Введите высоту первой матрицы: '))
for i in range(h):
    m.append(list(map(int,input().split(' '))))
h = int(input('Введите высоту второй матрицы: '))
for i in range(h):
    m2.append(list(map(int,input().split(' '))))
print('Выберите комманду (напишите цифру)')
print('1) Транспонирование матриц')
print('2) Умножение матриц')
print('3) Определение ранга матрицы')
kom = int(input())
if kom==1:
    m = transp(m)
    m2 = transp(m2)
    print('Транспонированные матрицы:')
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end=' ')
        print()
    print()
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            print(m2[i][j],end=' ')
        print()
elif kom == 2:
    proizved = proizv(m,m2)
    print('Произведение двух матриц:')
    for i in range(len(proizved)):
        for j in range(len(proizved[0])):
            print(proizved[i][j],end=' ')
        print()
