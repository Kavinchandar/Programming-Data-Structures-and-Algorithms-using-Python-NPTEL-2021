import random
import sys
sys.setrecursionlimit(100000)


def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1


def rquicksort_help(lst, low, high):
    if low <= high:
        pi = partition(lst, low, high)
        rquicksort_help(lst, low, pi-1)
        rquicksort_help(lst, pi+1, high)
        return lst


def rquicksort(lst):
    random.shuffle(lst)
    n = len(lst)-1
    return rquicksort_help(lst, 0, n)
