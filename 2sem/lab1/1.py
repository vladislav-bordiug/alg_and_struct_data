import time

def prostota(n):        #Функция для проверки простоты числа
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def naive(pattern, string):
    pattern_len = len(pattern)
    string_len = len(string)
    counter = 0
    for i in range(string_len - pattern_len + 1):   #Проходимся циклами по строке и находим шаблон
        letters_count = 0
        for j in range(pattern_len):
            if string[i + j] == pattern[j]:
                letters_count += 1
                if letters_count == pattern_len:    #Если нашли шаблон - прибавляем счетчик
                    counter += 1
            else:
                break
    return counter


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


def boyerMoore(pattern, string):
    pattern_len = len(pattern)
    string_len = len(string)
    offset = 0
    found_count = 0
    l = 0
    while offset + pattern_len - 1 < string_len:
        found = True
        for l in range(pattern_len - 1, -1, -1):
            if string[l + offset] != pattern[l]:
                found = False
                break

        if found:
            found_count += 1

        for l in range(pattern_len - 2, -1, -1):
            found_char = False
            if string[offset + pattern_len - 1] == pattern[l]:
                offset += pattern_len - 1 - l
                found_char = True
                break

        if not found_char:
            offset += pattern_len

    return found_count


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


def rabin_karp(pattern, string):
    alphabet = list(set(string + pattern))
    pattern_len = len(pattern) - 1
    string_len = len(string)
    alphabet_len = len(alphabet)
    pattern_hash = get_hash(pattern, pattern_len, alphabet, alphabet_len)
    counter = 0
    for i in range(string_len - pattern_len + 1):
        substr = string[i:i + pattern_len + 1]
        if get_hash(substr, pattern_len, alphabet, alphabet_len) == pattern_hash:
            if substr == pattern:
                counter += 1
    return counter


def get_hash(string, string_len, alphabet, alphabet_len):
    hash = 0
    for i in range(string_len + 1):
        hash += alphabet.index(string[string_len - 1 - i]) * alphabet_len ** i
    return hash

def find(function):
    now = [0] * 100
    global simple_string
    start = time.time()
    for i in range(10, 100):
        now[i] = function(f'{i}', simple_string)
    end = time.time()
    return end - start, function.__name__, now.pop(now.index(max(now))), now.pop(now.index(max(now)))

simple = []
k = 0
i = 2
while k != 500:
    if prostota(i):
        simple.append(str(i))
        k += 1
    i += 1

simple_string = ''.join(simple)
a = find(naive)
print(a[1],': время выполнения =', a[0],'Наиболее встречающиеся двузначные числа встречаются в файле',a[2],'раза и',a[3],'раз')
a = find(boyerMoore)
print(a[1],': время выполнения =', a[0],'Наиболее встречающиеся двузначные числа встречаются в файле',a[2],'раза и',a[3],'раз')
a = find(rabin_karp)
print(a[1],': время выполнения =', a[0],'Наиболее встречающиеся двузначные числа встречаются в файле',a[2],'раза и',a[3],'раз')
a = find(knut_morris_pratt)
print(a[1],': время выполнения =', a[0],'Наиболее встречающиеся двузначные числа встречаются в файле',a[2],'раза и',a[3],'раз')
