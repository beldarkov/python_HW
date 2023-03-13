number = int(input("Введите трехзначное число: "))
# проверка на введение трехзначного: 
# if number < 100 or number > 1000:
#     print("Введено не трехначное число!")
# else ->

# 1 вариант
sum = number // 100 + (number // 10) % 10  + number % 10
print(sum)
# # 2 вариант
# number = input("Введите трехзначное число: ")
# sum = int(number[0]) + int(number[1]) + int(number[2])
# print(sum)