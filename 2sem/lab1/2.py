import hashlib
ref = open('Корпоративные ценности.txt', 'r', encoding="utf8")
Wiki = open('Wiki.txt', 'r', encoding="utf8")

ref_str = []
for string in ref:
    ref_str.append(string[:-2])

Wiki_str = []
for string in Wiki:
    Wiki_str.append(string[:-2])

ref_one_string = ' '.join(ref_str)
Wiki_one_string = ' '.join(Wiki_str)

for i in '.,-!;:?()«»—–"[]':
    ref_one_string = ref_one_string.replace(f'{i}','')
    Wiki_one_string = Wiki_one_string.replace(f'{i}','')

ref_words = ref_one_string.split(' ')
ref.close()
Wiki_words = Wiki_one_string.split(' ')
Wiki.close()

ref_three = []
ref_hash = []
three_words = ''

for i in range(len(ref_words) - 2):
    three_words = ref_words[i] + ' ' + ref_words[i+1] + ' ' + ref_words[i+2]
    ref_three.append(three_words)
    cur_hash = hashlib.md5(three_words.encode())
    ref_hash.append(cur_hash.hexdigest())

Wiki_three = []
Wiki_hash = []
for i in range(len(Wiki_words) - 2):
    three_words = Wiki_words[i] + ' ' + Wiki_words[i+1] + ' ' + Wiki_words[i+2]
    Wiki_three.append(three_words)
    cur_hash = hashlib.md5(three_words.encode())
    Wiki_hash.append(cur_hash.hexdigest())

counter = 0
for i in range(len(Wiki_hash)):
    for j in range(len(ref_hash)):
        if Wiki_hash[i] == ref_hash[j]:
            if Wiki_three[i] == ref_three[j]:
                counter += 1
                print(Wiki_three[i])
        else:
            continue

print((counter / len(ref_words)*100))
