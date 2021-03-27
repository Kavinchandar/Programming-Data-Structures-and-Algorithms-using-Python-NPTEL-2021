def heapify(lst, i):
    root = i
    left = 2*i + 1
    right = 2*i + 2

    if left < len(lst) and lst[left] < lst[root]:
        root = left
    if right < len(lst) and lst[right] < lst[root]:
        root = right

    if root != i:
        lst[i], lst[root] = lst[root], lst[i]
        heapify(lst, root)


def minheap(lst):
    n = len(lst)
    lf = n//2 - 1
    for i in range(lf, -1, -1):
        heapify(lst, i)
    return lst[0]


lst = [1, 2]
print(minheap(lst))
