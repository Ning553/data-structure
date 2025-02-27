# 计数排序，时间复杂度只有 O(n) 但是有max_count的限制
from cal_time import *
import random,copy
@cal_time
def count_sort(ls,max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in ls:
        count[val] += 1
    ls.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            ls.append(ind)

@cal_time
def sys_sort(ls):
    ls.sort()

ls = [random.randint(0,100) for _ in range(100000)]

ls1 = copy.deepcopy(ls)
ls2 = copy.deepcopy(ls)
random.shuffle(ls1)
random.shuffle(ls2)
count_sort(ls1,100)
sys_sort(ls2)
# print(ls1)
# print(ls2)














# def count_sort(ls,max_count=10):
#     l = [0 for _ in range(max_count+1)]
#     # for i in range(len(ls)):
#     #     l[ls[i]] += 1
#     for val in ls:
#         l[val] += 1
#     return l
#
# ls = [1,2,3,4,5,6,7,8,0,0,1,2,3,3,3,5,10]
# l = count_sort(ls)
# print(l)
# for index,num in enumerate(l):
#     for i in range(num):
#         print(index,end=' ')

