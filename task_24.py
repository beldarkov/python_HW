N = int(input("Кол-во кустов: "))
berries = [2, 11, 3, 20, 5, 8]
# for i in range(N):
#     berries.append(int(input(f"Сколько ягод на {i + 1}-ом кусте: ")))
new_list = []
res = 0 
number = 0
for i in range(len(berries) - 1):
    new_list.append(berries[i] + berries[i - 1] + berries[i + 1])
new_list.append(berries[-2] + berries[-1] + berries[0])
res = max(new_list)
print(res)
