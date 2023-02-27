# Ты находишься в метро, ты помнишь, что на какой-то из станций стоит красивая
# скульптура, с которой ты не успел сфотографироваться в прошлый раз
# Задача: найти эту статую
graph = {}
graph["Сенная площадь"] = ["Горьковская", "Технологический институт", "Спасская"]
graph["Горьковская"] = []
graph["Технологический институт"] = ["Фрунзенская"]
graph["Фрунзенская"] = []
graph["Спасская"] = ["Достоевская"]
graph["Достоевская"] = ["Владимирская"]
graph["Владимирская"] = ["Технологический институт"]

from collections import deque

searched = set()
statuya = "Фрунзенская"

start = "Сенная площадь"


def poisk(name):
    if name == statuya:
        print("Статуя находится на станции метро", name)
        return True
    else:
        searched.add(name)
        queue = deque()
        queue += graph[name]
        for i in queue:
            if not i in searched:
                poisk(i)


poisk(start)
