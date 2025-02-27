import random
from cal_time import *
@cal_time
def bucket_sort(ls,n=100,max_num=10000):
    buckets=[[] for _ in range(n+1)]
    for val in ls:
        num_buckets = min(val//(max_num//n),n-1) # val 要放入的桶的编号
        bucket = buckets[num_buckets] # val 要放入的桶
        bucket.append(val) # 把val放到桶里
        for j in range(len(bucket)-1,0,-1): # 反向冒泡排序
            if bucket[j-1] > bucket[j]:
                bucket[j-1],bucket[j] = bucket[j],bucket[j-1]
            else:
                break
    soeted_ls=[]
    for bucket in buckets:
        soeted_ls.extend(bucket) # ls1.extend(iterable):可以将一个可迭代的数据（如列表，元组）的元素添加到ls1中
    return soeted_ls

ls=[random.randint(0,10000) for _ in range(1000)]
print(bucket_sort(ls),100,10000)
