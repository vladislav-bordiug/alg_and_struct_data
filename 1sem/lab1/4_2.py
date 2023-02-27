import timeit
import numpy as np
print('Введите матрицу 3x3')
a=[]
for i in range(3):
    a.append(list(map(float, input().split(' '))))
if np.linalg.det(a) != 0:
    time = timeit.timeit("np.linalg.inv(a)", number=1, globals=globals())
    itog = np.linalg.inv(a)
    print(itog)
    print('Время выполнения =',time)
else:
    print('Определитель матрицы равен нулю, обратной матрицы не существует')
