def generate_arithmetic_progression(a1, d, n):
    progression = [a1 + (i * d) for i in range(n)]
    return progression

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

progression = generate_arithmetic_progression(a1, d, n)

print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)
