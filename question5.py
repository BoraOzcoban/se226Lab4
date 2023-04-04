divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

united_we_stand = {**divided, **we_fall}

for name, age in united_we_stand.items():
    print(f'{name} {age}')

del united_we_stand['Nat']

for name, age in united_we_stand.items():
    print(f'{name} {age}')

for name, age in sorted(united_we_stand.items()):
    print(f'{name} {age}')

values = united_we_stand.values()
print('Maximum age:', max(values))
print('Minimum age:', min(values))