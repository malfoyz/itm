# 1
human = {
    'name': 'Сергей',
    'age': 21,
    'height': 167,
    'weight': 67,
    'foot size': 39,
}

print(human, '\n')

# 2
for key, value in human.items():
    print(key, human[key])
print()

# 3
human['foot size 2'] = 40
print(human, '\n')

# 4
del human['age']   # human.pop('age', None)
print(human)

