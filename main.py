import random
n = 5
arr = [random.randint(0,1) for _ in range(n)]
print(arr)
print(arr.count(0) if arr.count(0) < arr.count(1) else arr.count(1))
