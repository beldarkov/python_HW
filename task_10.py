import random
n = int(input("Введите кол-во монеток: "))
count1, count0 = 0, 0
for i in range(n):
    coin = random.randint(0, 1)
    if coin == 1:
        count1 += 1
    else:
        count0 += 1
print(count1 if count1 < count0 else count0)