lst = ['a', 's', '1', 'a', '32', '23']

letters = []
for symbol in lst:
    if symbol.isalpha():
        letters.append(symbol)

del letters[-1]
letters.reverse()   # lst [::-1]
print(letters)

