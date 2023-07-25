sum = 7
mtp = 12
a, b = 0, 0
for i in range(1000):
    for j in range(1000):
        if i + j == sum and i * j == mtp:
            a, b = i, j
print((a,b))
            