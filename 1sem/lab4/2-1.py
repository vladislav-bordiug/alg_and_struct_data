def block_sort(input_arr):
    x = min(input_arr) + (max(input_arr) - min(input_arr)) / 2 
    arr = [[], []]
    for i in input_arr:
        if i < x:
            arr[0].append(i)
        else:
            arr[1].append(i)
    result_arr = []
    for i in range(len(arr)):
        a = arr[i]
        if len(a) == 2:
            a[0], a[1] = min(a), max(a)
        if len(a) > 2 and max(a) != min(a):
            a = block_sort(a)
        for j in a:
            result_arr.append(j)
    return result_arr
print("Введите элементы списка через пробел")
arr = list(map(float, input().split()))
print(block_sort(arr))
