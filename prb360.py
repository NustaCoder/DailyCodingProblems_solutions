lst1 = [1, 7, 3]
lst2 = [2, 1, 6, 7, 9]
lst3 = [3, 9, 5]
lst = [0 for i in range(1, 10)]
lst_or = [lst1, lst2, lst3]

for i in lst_or:
    for j in i:
        lst[j-1] += 1
print(lst)
