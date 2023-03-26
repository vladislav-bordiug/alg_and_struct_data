# Создаем граф
graph = {
    'Tverskaya Street': {'Strastnoy Boulevard': 0.6, 'Okhotny Ryad': 1.2},
    'Strastnoy Boulevard': {'Tverskaya Street': 0.6, 'Pushkinskaya Square': 0.9},
    'Pushkinskaya Square': {'Strastnoy Boulevard': 0.9, 'Tverskaya Street': 1.4, 'Chekhovskaya Street': 1.2},
    'Chekhovskaya Street': {'Pushkinskaya Square': 1.2, 'Arbat Street': 1.4},
    'Arbat Street': {'Chekhovskaya Street': 1.4, 'Smolenskaya Square': 1.1},
    'Smolenskaya Square': {'Arbat Street': 1.1, 'Kutuzovsky Prospekt': 1.5},
    'Kutuzovsky Prospekt': {'Smolenskaya Square': 1.5, 'Novy Arbat Street': 1.3},
    'Novy Arbat Street': {'Kutuzovsky Prospekt': 1.3, 'Okhotny Ryad': 1.7},
    'Okhotny Ryad': {'Tverskaya Street': 1.2, 'Novy Arbat Street': 1.7}
}
infinity = float('inf')

# Создаем словарь с наименьшими путями, который в процессе будет обновляться
# Так как мы стартуем с Тверской улицы, попасть оттуда мы можем только на Страстной бульвар
# и Охотный ряд, поэтому для остальных наименьшая стоимость - бесконечность

costs = {
    'Tverskaya Street': 0,
    'Strastnoy Boulevard': 0.6,
    'Okhotny Ryad': 1.2,
    'Pushkinskaya Square': infinity,
    'Chekhovskaya Street': infinity,
    'Arbat Street': infinity,
    'Smolenskaya Square': infinity,
    'Kutuzovsky Prospekt': infinity,
    'Novy Arbat Street': infinity
}

# Создадим словарь с "родителями" вершины

parents = {
    'Strastnoy Boulevard': 'Tverskaya Street',
    'Okhotny Ryad': 'Tverskaya Street',
    'Pushkinskaya Square': None,
    'Chekhovskaya Street': None,
    'Arbat Street': None,
    'Smolenskaya Square': None,
    'Kutuzovsky Prospekt': None,
    'Novy Arbat Street': None
}

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')  #Фукнция находит вершину с наименьшим расстоянием, которая еще не была рассмотрена
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


processed = []
node = find_lowest_cost_node(costs)
while node is not None: # Пока не просмотрели все вершины
    cost = costs[node]
    neighbours = graph[node]    # Смотрим на соседей вершины
    for n in neighbours.keys():
        new_cost = cost + neighbours[n] # Расстояние от просматриваемой вершины до ее соседа
        if costs[n] > new_cost: # Если оно будет меньше, чем прежнее - обновляем значения
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)  # Добавляем вершину в список просмотренных
    node = find_lowest_cost_node(costs)

way = []
cur_street = 'Kutuzovsky Prospekt' # Пример: наименьшее расстояние от Тверской до Кузнецовского пр-та
way.append(cur_street)
while cur_street != 'Tverskaya Street': #Добавляем родителей, родителей родителей и т.д.
    cur_street = parents[cur_street]
    way.append(cur_street)
way.reverse()

print(f'Расстояние от Tverskaya Street до Kutuzovsky Prospekt: {costs["Kutuzovsky Prospekt"]}')
print(' -> '.join(way))