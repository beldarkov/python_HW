ticket = input("Введите номер билета: ")
sum1, sum2 = 0, 0
for i in ticket[0:(len(ticket) // 2)]:
    sum1 += int(i)
for i in ticket[(len(ticket) // 2):len(ticket)]:
    sum2 += int(i)
print("yes" if sum1 == sum2 else "no")