import random,copy
from cal_time import *
# 基数排序 radix sort : O(n) 是线性时间复杂度哦，NICE!

@cal_time
def radix_sort(ls):
    max_num = max(ls)
    t = 0
    while 10 ** t <= max_num:
        buckets = [[] for _ in range(10)]
        for val in ls:# 679 --> First: 679 % 10 --> 9 Second: 679//10 --> 67 --> 67%10 -->7 3th: 679 //100 -->6 --> 6%10-->6
            num = (val // (10 ** t)) % 10 #桶的编号
            buckets[num].append(val)
        ls.clear()
        for bucket in buckets:
            ls.extend(bucket)
        t += 1
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
@cal_time
def quick_sort_2(ls, left, right):
    return quick_sort(ls, left, right)

# ls = list(range(1000000))
ls = [random.randint(0,1000000000000) for _ in range(100000)]
random.shuffle(ls)
ls1 = copy.deepcopy(ls)
ls2 = copy.deepcopy(ls)

radix_sort(ls1) # kn k = log(10,n)
quick_sort_2(ls2,0,len(ls2)-1) # nlogn log(2,n)
# print(ls)