def Binarysearch(lst, x):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low+(high-low) // 2
        if lst[mid] == x:
            return True
        if x > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


lst = [1, 2, 3, 4, 5, 5, 6, 7, 6, 7, 9, 0, 10]
lst.sort()
print(lst)
x = int(input())
if Binarysearch(lst, x):
    lst.remove(x)
print(lst)
