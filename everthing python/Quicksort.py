
def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] >= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1


def quiksort_help(lst, low, high):
    if low <= high:
        p = partition(lst, low, high)
        quiksort_help(lst, low, p-1)
        quiksort_help(lst, p+1, high)
    return lst


def quiksort(lst):
    n = len(lst) - 1
    return quiksort_help(lst, 0, n)


lst = [1, 3, 2]
print(quiksort(lst))
