import random

def find_indices_in_range(lst, min_val, max_val):
    indices = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            indices.append(i)
    return indices

lst = [random.randint(-100, 100) for _ in range(6)]
print("Сгенерированный список:", lst)

min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))
    
indices = find_indices_in_range(lst, min_val, max_val)
    
if len(indices) > 0:
    print("Индексы элементов в заданном диапазоне:", indices)
else:
        print("Нет элементов в заданном диапазоне.")