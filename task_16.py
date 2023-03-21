N = int(input())
my_list = []
for _ in range(N):
    my_list.append(int(input()))
X = int(input())
count = 0
for i in my_list:
    if X == my_list[i - 1]:
        count += 1
print(count)