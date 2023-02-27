import timeit
def det(matrix):        #ф-ция для нахождения определителя матрицы
    d1 = (matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]) #опр. для первой матрицы 2*2
    matrix[0][0] = d1 * matrix[0][0] * (1) #умножаем элемент матрицы на его минор и не забываем про кофактор(знаки + или -)
    #проделываем ту же операцию для остальных элементов первой строки
    d2 = matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0] 
    matrix[0][1] = d2 * matrix[0][1] * (-1)
    d3 = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    matrix[0][2] = matrix[0][2] * d3 * (1) 
    return sum(matrix[0]) #определителем будет являться сумма всех элементов в первой строке
#транспонирование матрицы (замена строк на столбцы относительно главной диагонали)
def transport(m):
    mnew=[[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            mnew[i][j]=m[j][i]
    return mnew
#определители всех матриц 2x2 для каждых двух строк
def oprs(ml):
    mb = [0]*3
    mb[0] = ml[0][1]*ml[1][2]-ml[0][2]*ml[1][1]
    mb[1] = ml[0][0]*ml[1][2]-ml[0][2]*ml[1][0]
    mb[2] = ml[0][0]*ml[1][1]-ml[0][1]*ml[1][0]
    return mb
def reverse(m):
    mreversed=[[0 for x in range(3)] for y in range(3)]
    mt=transport(m)
    opr_m = det(m)
    if opr_m == 0:
        return 0
    #определители для двух последних строк
    ml = [mt[1],mt[2]]
    mreversed[0] = oprs(ml)
    #нам нужна матрица кофакторов, для первой строки нужно поменять знак второго элемента
    mreversed[0][1]*=-1
    #определители для первой и третьей строк
    ml = [mt[0],mt[2]]
    mreversed[1] = oprs(ml)
    #для второй строки нужно поменять знак первого и третьего элементов
    mreversed[1][0]*=-1
    mreversed[1][2]*=-1
    #определители для первой и второй строк
    ml = [mt[0],mt[1]]
    mreversed[2] = oprs(ml)
    #для третьей строки нужно поменять знак второго элемента
    mreversed[2][1]*=-1
    #делим каждый элемент на определитель
    for i in range(3):
        for j in range(3):
            mreversed[i][j]=mreversed[i][j]/opr_m
    return mreversed
print('Введите матрицу 3x3')
a=[]
for i in range(3):
    a.append(list(map(float, input().split(' '))))
itog = reverse(a)
time = timeit.timeit("reverse(a)", number=1, globals=globals())
if itog == 0:
    print('Определитель равен нулю, обратной матрицы не существует')
else:
    for i in range(3):
        for j in range(3):
            print(itog[i][j],end=' ')
        print()
print('Время выполнения =',time)
