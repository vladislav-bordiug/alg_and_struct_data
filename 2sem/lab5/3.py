import copy
results = []
m=[0,0,0,0,0,0,0,0]

#из условия следует, что все 8 ферзей расположены на разных 8 строках
#поэтому надо только найти координаты по столбцам, отвечающие условию

#проверка на то, что ферзь не будет находиться в одном столбце или на одной диагонали с предыдущими
def check(x,y):
    for i in range(x):
        if m[i] == y or abs(i-x) == abs(m[i] - y):
            return False
    return True
#функция, которая находит все варианты
def res(i):
    #если 8 ферзей расположили, то выходим
    if i == 8:
        r = copy.deepcopy(m)
        results.append(r)
        return
    # иначе перебираем все возможные варианты
    else:
        for j in range(8):
            if check(i,j):
                m[i] = j
                res(i+1)
field = \
    [['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

res(0)

print('All variants to locate eight queens so that no two queens will be located on the same horizontal, vertical or diagonal \n(considering not only two big diagonals, * is a queen):')

for x in results:
    fieldy = copy.deepcopy(field)
    for i in range(len(x)):
        fieldy[i][x[i]] = '*'
    for m in fieldy:
        print(m)
    print()
