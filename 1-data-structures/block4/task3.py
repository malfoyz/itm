lst = ['a', 's', '1', 'a', '32', '23']

# 1
# letters = [lst[0], lst[1], lst[3]]
# numbers = [lst[2], lst[4], lst[5]]
# print(letters, numbers)

letters, numbers = [], []
for symbol in lst:
    if symbol.isdigit():
        numbers.append(symbol)
    if symbol.isalpha():
        letters.append(symbol)
print(letters, numbers)