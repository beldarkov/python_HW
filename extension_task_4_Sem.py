def get_binary_octal_representation(num):
    binary = bin(num)[2:]
    octal = oct(num)[2:]
    return binary, octal

binary, octal = get_binary_octal_representation(int(input('Введите число: ')))
print(f'Двоичное представление: {binary}')
print(f'Восьмиричное представление: {octal}')