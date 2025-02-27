def selection_sort(ls):
    for i in range(len(ls)-1):
        min_index = i
        for j in range(i+1,len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[min_index], ls[i] = ls[i], ls[min_index]

ls =[7,1,8,9,2,5,4,3]
selection_sort(ls)
print(ls)