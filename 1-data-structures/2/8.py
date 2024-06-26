a = int(input('Введите двузначное число: '))
left, right = a // 10, a % 10
print(f'Перевернутое число = {right * 10 + left}')