
def insert_sort(ls):
    for i in range(1,len(ls)):#表示摸到的牌的下标
        j  = i - 1 #手里有的最右边的牌
        tmp = ls[i] # 用 tmp 存住 ls[i] 避免给覆盖掉了
        while j >= 0 and tmp <= ls[j]:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1]=tmp
        # print(ls)


ls =[7,1,8,9,2,5,4,3]
insert_sort(ls)
print(ls)