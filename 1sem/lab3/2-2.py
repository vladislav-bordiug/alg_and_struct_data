def sort(m):
    if len(m)>1:
        mid = len(m)//2
        l = m[:mid]
        r = m[mid:]
        sort(l)
        sort(r)
        i=0
        j=0
        k=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                m[k]=l[i]
                i+=1
            else:
                m[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            m[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            m[k]=r[j]
            j+=1
            k+=1
print("Введите массив чисел через пробел")
arr = list(map(int, input().split()))
sort(arr)
print(arr)
print("Сложность алгоритма O(nlog(n))")
