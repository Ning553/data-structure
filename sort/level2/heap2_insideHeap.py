import heapq # heap queue 优先队列
import random

ls = [i for i in range(10)]
random.shuffle(ls)
print(ls)
heapq.heapify(ls) # 建堆，默认建的是小根堆
# print(ls)
# for i in range(len(ls)):
#     print(heapq.heappop(ls),end=' ')
new_ls = [heapq.heappop(ls) for _ in range(len(ls))]
# 在 for 循环中，如果不需要使用循环变量，可以使用下划线（_）来代替
print(new_ls)


