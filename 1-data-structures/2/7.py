a = int(input('Введите двузначное число: '))
left, right = a // 10, a % 10
summ, comm = left + right, left * right
print(f'Сумма цифр = {summ}, произведение цифр = {comm}')