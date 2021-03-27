def selectionsort(lst):
    n = len(lst)
    for i in range(n):
        minpos = i
        for j in range(i, n):
            if lst[j] < lst[minpos]:
                minpos = j
        lst[i], lst[minpos] = lst[minpos], lst[i]
    return lst
