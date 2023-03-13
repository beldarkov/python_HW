total_Count = int(input("Сколько всего сделали? - "))
petya_Count = total_Count // 6
serezha_Count = petya_Count
katya_Count = (petya_Count + serezha_Count) * 2
print(f"{total_Count} - > {petya_Count} {katya_Count} {serezha_Count}")