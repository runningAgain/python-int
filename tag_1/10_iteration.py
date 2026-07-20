""" 
Über Listen iterieren: for loop
"""
names = ["Bob", "Alice", "Grumpy"]
print(names)

# good practice: Singular und Plural
for name in names:
    print(name)


# Liste filtern: neue Liste erstellen mit Werten > 3
values = [1, 2, 3, 4, 5, 6, 7]
filtered_values = []
for value in values:
    if value > 3:
        filtered_values.append(value)

print(f"Bereinigte Liste: {filtered_values}")