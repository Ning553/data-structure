def bubble_sort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1],ls[j]

ls = list(range(100))
import random
random.shuffle(ls)
print(ls)
bubble_sort(ls)
print(ls)

def selection_sort(ls):
    min_i = 0
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[j] < ls[min_i]:
                min_i = j
        ls[i], ls[min_i] = ls[min_i],ls[i]
ls = list(range(100))
import random
random.shuffle(ls)
print(ls)
bubble_sort(ls)
print(ls)