def get_password(n):
    password = ""
    for i in range(1, n - 1):
        j = i + 1
        while j < n:
            if n % (i + j) == 0:
                password += f'{i}{j}'
            j += 1
    return password

number = int(input('Введите число от 3 до 20 включительно: '))
print(get_password(number))