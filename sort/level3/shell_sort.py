from copy import deepcopy
from cal_time import *

# 带有 gap 的插入排序。 希尔排序 shell sort 就是建立在插入排序的基础上进行的
# 希尔排序的时间复杂度和 gap 有关
def insertion_sort_gap(ls,gap):
    for i in range(gap, len(ls)):
        tmp = ls[i]
        j = i - gap
        while j >= 0 and ls[i] < ls[j]:
            ls[j+gap] = ls[j]
            j -= gap
        ls[j+gap] = tmp

@ cal_time
def shell_sort(ls):
    gap = len(ls)//2
    while gap > 0:
        insertion_sort_gap(ls,gap)
        gap = gap//2


@ cal_time
def insert_sort(ls):
    for i in range(1,len(ls)):#表示摸到的牌的下标
        j  = i - 1 #手里有的最右边的牌
        tmp = ls[i] # 用 tmp 存住 ls[i] 避免给覆盖掉了
        while j >= 0 and tmp <= ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1]=tmp

def sift(ls,low,high):
    i = low # 指向 low，最开始为根节点
    j = 2*i+1 #指向 i指向结点的左孩子
    tmp = ls[low] #
    while j <= high: # 没有超界，就执行以下操作
        if j+1 <= high and ls[j+1] > ls[j]: # 右孩子存在并且右孩子的值大于左孩子，把 j 指向右孩子 [ <= 要注意！！！]
            j = j+1
        if ls[j] > tmp: # 孩子的值大于父亲
            ls[i] = ls[j] # 孩子上移
            i = j #到下一层
            j = i*2+1
        else: # ls[j] <= tmp
            ls[i] = tmp # 把 tmp放到某个领导层
            break
    else:
        ls[i] = tmp # tmp 放到叶子结点

@ cal_time
def heap_sort(ls):
    n = len(ls)
    # 先建堆
    for i in range((n-2)//2,-1,-1):
        sift(ls,i,n-1)
    # 建堆完成，下面开始堆排序。从最后一位开始遍历。【最后一个与根节点交换 -- 根节点放到最后一个位置 -- 最后一个位置向前 (high = i-1) -- 调整 sift】
    for i in range(n-1,-1,-1):
        ls[0], ls[i] = ls[i],ls[0]
        sift(ls,0,i-1)

ls = list(range(10000))
import random
random.shuffle(ls)
ls1 = deepcopy(ls)
ls2 = deepcopy(ls)
ls3 = deepcopy(ls)

shell_sort(ls1)
insert_sort(ls2)
heap_sort(ls3)

# 速度 ： 堆排序 > 希尔排序 > 插入排序

