# 取出一个队列中最大的几个数

def sift(ls,low,high):
    i = low
    j = 2*i+1
    tmp = ls[low]
    while j <= high:
        if j+1 <= high and ls[j+1] < ls[j]:
            j = j+1
        if ls[j] < tmp:
            ls[i] = ls[j]
            i = j
            j = 2*i+1
        else:
            ls[i] = tmp
            break
    ls[i] = tmp
# 小根堆调整
def top_k(ls,k):
    heap = ls[:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    # 1. 建堆
    for i in range(k,len(ls)):
        if ls[i] > heap[0]:
            heap[0] = ls[i]
            sift(heap,0,k-1)
    # 2. 遍历
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)
    # 3. 出数
    return heap

ls = [7,4,8,0,1,3,9,5,6,11,10]
print(top_k(ls,6))
