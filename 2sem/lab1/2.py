def prefix(string):
    pre_len = len(string)
    prefixes = [0] * pre_len

    for i in range(pre_len):
        substr = string[:i + 1]
        count = 0
        for j in range(len(substr)):
            if substr[:j] == substr[-j:]:
                count = j
        prefixes[i] = count
    return prefixes


def knut_morris_pratt(pattern, string):
    pattern_prefixes = prefix(pattern)
    counter = 0
    string_len = len(string)
    pattern_len = len(pattern)
    i = 0
    j = 0
    while i < string_len:
        if string[i] == pattern[j]:
            i += 1
            j += 1
            if j == pattern_len:
                counter += 1
                j = pattern_prefixes[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = pattern_prefixes[j - 1]
    return counter


ref = open('Корпоративные ценности.txt', 'r', encoding="utf8")
Wiki = open('Wiki.txt', 'r', encoding="utf8")

ref_str = []
for string in ref:
    ref_str.append(string[:-2]) #Добавляем строки из реферата в список

Wiki_str = []
for string in Wiki:
    Wiki_str.append(string[:-2])      #Добавляем строки из статьи вики в список

ref_one_string = ' '.join(ref_str)     #Объединяем все строки в одну большую строку
Wiki_one_string = ' '.join(Wiki_str)

for i in '.,-!;:?()«»—–"[]':
    ref_one_string = ref_one_string.replace(f'{i}','') #Убираем все ненужные символы из строки, оставляем слова
    Wiki_one_string = Wiki_one_string.replace(f'{i}','')

ref_words = ref_one_string.split(' ')    #Разбиваем по пробелу - составляем список слов
ref.close()
Wiki.close()

ref_len = len(ref_one_string)
plagiat_syms = 0

for rl in range(len(ref_words) - 2):
    search_str = " ".join(ref_words[rl: rl + 3])    #Составляем 3 слова
    count_found = knut_morris_pratt(search_str, Wiki_one_string)    #Применяем поиск КНП
    plagiat_syms += len(search_str) * count_found   #Считаем кол-во найденных символов

plagiat = plagiat_syms / ref_len
print('В файле',round(plagiat * 100,2),'% плагиата')
