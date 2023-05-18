#функция, находящая наименьшее пропущенное число
#в худшем случае она проходит 2 раза по массиву, а на каждом последующем шаге делит его пополам
#т.е. сложность <= 2n+n+n/2+n/4+...=2n*(1-(1/2)^log2(n))/(1-1/2)=
#=2n*(1-2^log2((n)^(-1)))/(1-1/2)=2n*(1-1/n)/(1/2)=4n-4
#тогда зависимость линейная O(n)
def find(minimum,maximum,list):
    #если совпали, то осталось одно минимальное пропущенное число, получившееся число - ответ
    if minimum == maximum:
        return minimum
    #вычисляем середину
    middle = (maximum + minimum)//2
    #массив чисел, меньших или равных середине
    b = [x for x in list if x <= middle]
    #если среди чисел от minimum до middle есть пропущенное, то вызываем для них
    if len(b)<middle-minimum+1:
        return find(minimum,middle,b)
    #если есть пропущенное среди чисел от middle+1 до maximum, то вызываем для них
    else:
        return find(middle+1,maximum,[x for x in list if x > middle])

list = list(map(int,input('Enter a list of numbers separated by spaces:\n').split()))
minimum = min(list)
maximum = max(list)
if maximum - minimum + 1 != len(list):
    result = find(minimum,maximum,list)
    print('Minimal element which is not located in this list:',result)
else:
    print('There are no missing items in this list')
