def heapify(lst, i):
    n = len(lst)
    root = i
    left = 2*i+1
    right = 2*i+2

    if left < n and lst[left] > lst[root]:
        root = left

    if right < n and lst[right] > lst[root]:
        root = right

    if root != i:
        lst[i], lst[root] = lst[root], lst[i]
        heapify(lst, root)
    return lst


def max_heap(lst):
    n = len(lst)
    leaf_nodes = n//2 - 1
    for i in range(leaf_nodes, -1, -1):
        heapify(lst, i)
    return lst


def delmax(lst):
    n = len(lst)
    lst[0] = lst[n-1]
    lst = lst[:n-1]
    heapify(lst, 0)
    return lst


def insert(lst, x):
    lst.append(x)
    return max_heap(lst)


lst = [1, 3, 5, 4, 6, 13,
       10, 9, 8, 15, 17]


n = len(lst)
lst = insert(lst, 18)
print(lst[-1])
