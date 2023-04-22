import random


n = int(input('Количество экспонатов: '))  # Узнаем количество экспонатов
m = int(input('Количество заходов: '))  # Количество заходов
k = int(input('Количество кг за один заход: '))  # Количество килограмм за один заход

things = []
for i in range(n):     # Создаем список с товарами
    cost = random.randint(100, 3000)   # Присваиваем им рандомные стоимость и вес
    weight = random.randint(1, 10)
    things.append((cost, weight))

stolen_things = []   # Создаем список украденых вещей
steal_sum = 0   #Стоимость украденного

for l in range(m): #Количество заходов в музей
    n = len(things) #Каждый раз таблица будет разных размеров, потому что какие-то вещи воруем
    table_of_costs = [[0 for i in range(k+1)] for j in range(n+1)]   #Создаем список, который будем динамически заполнять
    stole_every_step = [[[] for i in range(k+1)]for j in range(n+1)] #Таблица, в которую будем заносить индексы украденных вещей на каждом шаге
    for i in range(1, n+1):
        for w in range(1, k+1):
            if things[i - 1][1] <= w: #Проверяем, вмещается ли текущий экспонат в рюкзак
                if table_of_costs[i - 1][w] > table_of_costs[i - 1][w - things[i - 1][1]] + things[i - 1][0]: #Выбираем максимальный элэлемент из предыдущего или текущего + украденного на  (k - вес товара)
                    table_of_costs[i][w] = table_of_costs[i-1][w]
                    stole_every_step[i][w] += stole_every_step[i-1][w]
                else:
                    table_of_costs[i][w] = table_of_costs[i - 1][w - things[i - 1][1]] + things[i - 1][0]
                    stole_every_step[i][w] += stole_every_step[i - 1][w - things[i - 1][1]]
                    stole_every_step[i][w].append(i-1)
            else:  #Если не можем поместить в рюкзак, то просто берем предыдущий за максимальное значение
                table_of_costs[i][w] = table_of_costs[i - 1][w]
                stole_every_step[i][w] += stole_every_step[i - 1][w]
    steal_sum += table_of_costs[n][k] #Наибольшая возможная стоимость будет хранится в последней ячейке

    cur_thing = []
    for ind in range(n):  #Воруем товары, если их индексы есть в последней ячейке stole_every_step
        if ind in stole_every_step[n][k]:
            stolen_things.append(things[ind])
        else:
            cur_thing.append((things[ind]))
    things = cur_thing

print('Товары, которые нужно украсть, чтобы получить наибольшую прибыль:')
print(stolen_things)
print(f'Прибыль составит: {steal_sum}')
