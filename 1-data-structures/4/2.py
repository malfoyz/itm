lst = ['Ростов', '+', 'на', '-', 'Дону']
lst[1] = '-'

# print(lst[0] + lst[1] + lst[2] + lst[3] + lst[4])
print(*lst, sep='')