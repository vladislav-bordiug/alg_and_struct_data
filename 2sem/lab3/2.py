import random

n = int(input())  # Узнаем количество экспонатов
m = int(input())  # Количество заходов
k = int(input())  # Количество килограмм за один заход

#things = [(3000, 30), (2000, 20), (1500, 15)]  #Пример набора, на котором жадный работает неправильно(

things = []
for i in range(n):     # Создаем список с товарами
    cost = random.randint(100, 3000)   # Присваиваем им рандомные стоимость и вес
    weight = random.randint(1, 10)
    things.append((cost, weight))

things.sort(key=lambda x:x[0])
things.reverse()    # Упорядочиваем  товары по убыванию стоимости
print(things)
stolen_things = []   # Создаем список украденых
for i in range(m):   # Делаем несколько заходов в наш музей
    cur_k = k
    j = 0
    while j < len(things):
        if cur_k < things[j][1]:    # Берем вещь с наибольшей стоимостью, которую еще можем унести
            j += 1
            continue

        else:
            cur_k -= things[j][1]  # Берем вещь с наибольшей стоимостью, которую еще можем унести
            stolen_things.append(things.pop(j))  # Убираем из списка украденную вещь и добавляем в список украденного
print(stolen_things)


