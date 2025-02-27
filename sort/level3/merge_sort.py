"""
一个列表，两段有序，将列表整段整成有序，这样的一个过程叫做一次归并

"""

def merge(ls,low,mid,high):
    i = low
    j = mid+1
    ltmp = []
    while i <= mid and j <= high:
        if ls[i] < ls[j]:
            ltmp.append(ls[i])
            i += 1
        else:
            ltmp.append(ls[j])
            j += 1
    while i <= mid:
        ltmp.append(ls[i])
        i += 1
    while j <= high:
        ltmp.append(ls[j])
        j += 1
    ls[low:high+1] = ltmp

def merge_sort(ls,low,high):
    if low < high:
        mid = (low+high)//2
        merge_sort(ls,low,mid)
        merge_sort(ls,mid+1,high)
        merge(ls,low,mid,high)

import random
ls = [i for i in range(5)]
random.shuffle(ls)
print(ls)
merge_sort(ls,0,len(ls)-1)
print(ls)