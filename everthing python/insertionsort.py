def insertionsort(lst):
    n = len(lst)
    for i in range(n):
        pos = i
        while(pos > 0 and lst[pos] < lst[pos-1]):
            lst[pos], lst[pos-1] = lst[pos-1], lst[pos]
            pos -= 1
    return lst
