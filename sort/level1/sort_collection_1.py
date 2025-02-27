# Low B 三人组 ：冒泡排序，选择排序和插入排序，时间复杂度都是 O(n2)
from cal_time import *

@cal_time
def  bubble_sort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-1-i):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]


ls = list(range(10000))
print('原序列：',ls)
bubble_sort(ls)
print('冒泡排序：',ls)
print('-'*40)

@cal_time
def select_sort(ls):
    for i in range(len(ls)-1):
        min_index = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[i],ls[min_index] = ls[min_index],ls[i]
ls2 =  list(range(10000))
print('原序列：',ls2)
select_sort(ls2)
print('选择排序：',ls2)

print('-'*40)

@cal_time
def insertion_sort(ls):
    for i in range(1,len(ls)):
        j = i - 1
        tmp = ls[i]
        while j >= 0 and tmp<=ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = tmp
ls3 = list(range(10000))
print('原序列：',ls3)
insertion_sort(ls3)
print('插入排序：',ls3)