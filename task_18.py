N = int(input("N - "))
lst = []
for i in range(N):
    lst.append(int(input()))
X = int(input("Х - "))
new_list = []
res = 0
for i in range(len(lst)):
    new_list.append(abs(X - lst[i]))
    if new_list[i] == min(new_list):
       res = lst[i]
print(f"Ближайшее к {X} - {res}")
    
