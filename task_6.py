ticket = input("Введите номер билета: ")
# 1 вариант
sum1, sum2 = 0, 0
for i in ticket[0:(len(ticket) // 2)]:
    sum1 += int(i)
for i in ticket[(len(ticket) // 2):len(ticket)]:
    sum2 += int(i)
print("yes" if sum1 == sum2 else "no")

# # 2 вариант
# sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2]) 
# sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5]) 
# print("yes" if sum1 == sum2 else "no")