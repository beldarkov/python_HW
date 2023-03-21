lst1, lst2 = [1, 23, 4, 5, 3, 8, 9], [2, 17, 3, 4, 9, 8]
lst_res = []
if len(lst1) > len(lst2):
    for i in lst1:
        for j in lst2:
            if j == i:
                lst_res.append(j)
else:
    for i in lst2:
        for j in lst1:
            if j == i:
                lst_res.append(j)
lst_res.sort()
for i in lst_res:
    print(i)