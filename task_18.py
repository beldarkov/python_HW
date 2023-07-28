
list_1 = [1, 2, 3, 4, 5]
k = 6
new_list = []
res = 0
for i in range(len(list_1)):
    new_list.append(abs(k - list_1[i]))
    if new_list[i] == min(new_list):
       res = list_1[i]
print(res)
    
