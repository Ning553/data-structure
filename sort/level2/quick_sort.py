def partition(ls, left , right):
    tmp = ls[left]
    while left < right:
        while left < right and ls[right] >= tmp:
            right -= 1
        ls[left] = ls[right]
        while left < right and ls[left] <= tmp:
            left += 1
        ls[right] = ls[left]
    ls[left] = tmp
    return left

def quick_sort(ls, left, right):
    if left < right:
        mid = partition(ls, left, right)
        quick_sort(ls, left, mid - 1)
        quick_sort(ls,mid + 1, right)

ls = list(range(100))
import random
random.shuffle(ls)
print(ls)
quick_sort(ls,0,len(ls)-1)
print(ls)