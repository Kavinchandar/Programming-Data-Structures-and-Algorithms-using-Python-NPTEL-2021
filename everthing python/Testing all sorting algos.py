from mergesort import *
from Quicksort import *
from randomized_quick_sort import *
from selectionsort import *
from insertionsort import *
import random

lst = [random.randint(-7500, 7500)
       for _ in range(random.randint(1, 100))]

print('Given List :\n', lst)
print('')
print('Sorted using Mergesort :\n', mergesort(lst))
print('')
print('Sorted using Quicksort :\n', quiksort(lst))
print('')
print('Sorted using Randomized Quicksort :\n', rquicksort(lst))
print('')
print('sorted using Selectionsort :\n', selectionsort(lst))
print('')
print('Sorted using Insertionsort :\n', insertionsort(lst))
