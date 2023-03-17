S, P = int(input("Введите сумму чисел: ")), int(input("Введите произведение чисел: "))
x, y = 0, 0
for i in range(S):
    for j in range(P):
        if i + j == S and i * j == P:
            x, y= i, j 
print(x, y)