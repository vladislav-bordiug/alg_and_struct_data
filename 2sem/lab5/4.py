n = int(input('Enter the number of stages\n')) #Вводим кол-во ступенек

steps = [0] * (n+2) #Создаем таблицу, где будем подсчитывать кол-во способов подняться на n-тую ступень
steps[2] = 1 #n-ая ступень будет под индексом k+1

for i in range(3,n+2):  #Заполняем таблицу
    steps[i] = steps[i-1] + steps[i-2] + steps[i-3] #на n-ую ступень можно попасть из n-1, n-2 и n-3

print('Number of options: ',steps[n+1]) #Под n+1 индексом n-ая ступенька
