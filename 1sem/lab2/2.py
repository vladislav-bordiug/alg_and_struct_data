people = {"110110": "Абдрахманов Мартин",
          "010001": "Бархатова Наташа",
          "101101": "Белоус Ярослав",
          "101010": "Филиппов Леонид",
          "101110": "Бордюг Владислав",
          "110010": "Буров Глеб",
          "100001": "Ветошкин Ростислав",
          "111010": "Влазнев Данила",
          "110111": "Власов Александр",
          "111001": "Даниленко Дмитрий",
          "110001": "Денисов Илья",
          "011111": "Егорова Валерия",
          "001001": "Зайнулина Алина",
          "101011": "Зенкин Даниил",
          "010111": "Ишанова Надежда",
          "000011": "Калачева Вера",
          "110100": "Клопов Михаил",
          "110011": "Колсанов Ярослав",
          "111111": "Коршунов Кирилл",
          "010110": "Крашенинникова Даша",
          "001111": "Куцак Анастасия",
          "110101": "Маноменов Иван",
          "100111": "Марков Даниил",
          "101001": "Панает Витя",
          "111110": "Париш Павел",
          "010010": "Рудкина Дарья",
          "010000": "Петрова Виктория",
          "010011": "Соколова Дарья",
          "000001": "Трофимцева Катя",
          "101111": "Федоров Влад",
          "101100": "Цховребов Андрей"}

questions = ['Загаданный человек - мужчина?','У загаданного человека светлые волосы?',
             'У загаданного человека карие глаза?','Загаданный человек из Санкт-Петербурга?',
             'Загаданный человек предпочитает питаться дома?',
             'В профиле Вконтакте у загаданного человека настоящая фотография?'
print(people.popitem("101100": ""))
st = ""
for i in range(6):
    print(questions[i])
    x = input()
    if x == "Да" or x=="ДА" or x == "да":
        st += "1"
    else:
        st += "0"
if people.get(st) != None:
    print("Вы загадали человека, которого зовут", people.get(st))
else:
    print("Такого человека в группе К3123 нет!")
