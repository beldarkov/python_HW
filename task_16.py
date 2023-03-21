N = int(input("N - "))
my_list = []
for _ in range(N):
    my_list.append(int(input()))
X = int(input("X - "))
count = 0
for i in range(len(my_list)):
    if my_list[i] == X:
        count += 1
print(count)