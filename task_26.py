def my_grade(a, b):
    if b == 0:
        return 1
    return a * my_grade(a, b - 1)
print(my_grade(2, 5))
