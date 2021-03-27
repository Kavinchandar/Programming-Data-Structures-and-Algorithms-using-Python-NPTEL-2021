def merge(l1, l2):
    c, m, n = [], len(l1), len(l2)
    i, j = 0, 0
    while i+j < m+n:
        if i == m:
            c.append(l2[j])
            j = j+1
        elif j == n:
            c.append(l1[i])
            i = i+1
        elif l1[i] <= l2[j]:
            c.append(l1[i])
            i = i+1
        elif l1[i] > l2[j]:
            c.append(l2[j])
            j = j+1
    return c


def mergesort(l):
    n = len(l)
    if n < 2:
        return l
    else:
        left = mergesort(l[:n//2])
        right = mergesort(l[n//2:])
        return merge(left, right)
