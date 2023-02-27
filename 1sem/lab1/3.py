import numpy as np
m_1 = []
m2_1 = []
h = int(input('Введите высоту первой матрицы: '))
for i in range(h):
    m_1.append(list(map(int,input().split(' '))))
h = int(input('Введите высоту второй матрицы: '))
for i in range(h):
    m2_1.append(list(map(int,input().split(' '))))
m = np.array(m_1)
m2 = np.array(m2_1)
print('Выберите комманду (напишите цифру)')
print('1) Транспонирование матриц')
print('2) Умножение матриц')
print('3) Определение ранга матрицы')
kom = int(input())
if kom==1:
    m = m.transpose()
    m2 = m.transpose()
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
    proizv = np.matmul(m,m2)
    print('Произведение двух матриц:')
    for i in range(len(proizv)):
        for j in range(len(proizv[0])):
            print(proizv[i][j],end=' ')
        print()
else:
    print('Ранк первой матрицы = ', np.linalg.matrix_rank(m))
    print('Ранк второй матрицы = ', np.linalg.matrix_rank(m2))
