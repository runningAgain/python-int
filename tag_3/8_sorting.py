"""
Sortieren (von Sequenzen und Dicts)
"""

liste = [1, 5, 2, 9, 7, 2]
liste.sort()

# Sorted erzeugt eine neue, sortierte Liste
liste = [1, 5, 2, 9, 7, 2]
sorted_list = sorted(liste, reverse=True)
print(sorted_list)

# Chars
chars = ["a", "f", "c", "d", "e"]
print(ord("a"))
sorted_chars = sorted(chars)
print(sorted_chars)


# def sort_function(el: str) -> str:
#     return el.lower()


chars = ["a", "f", "A", "B", "c", "b", "a", "d", "e"]
# schatt ["a", "f", "a", "b", "c", "b"....]
sorted_chars = sorted(chars, key=lambda el: el.lower())
# a A a
print(sorted_chars)


ids = ["id5", "idx1", "id2", "idy5", "id4", "id3"]
ids_sorted = sorted(ids, key=lambda el: int(el[-1]))
print(ids_sorted)

snacks = {"Milka": 3.30, "Kekse": 5.20, "Snickers": 1.50}
# sortiert nach Preis
# [1.5, 3.3, 5.2]
sorted_snacks = sorted(snacks.items(), key=lambda el: el[-1])
print(sorted_snacks)

print(list(snacks))  # ['Milka', 'Kekse', 'Snickers']
print(snacks.items())  # [('Milka', 3.3), ('Kekse', 5.2), ('Snickers', 1.5)]


# Nach Preis sortieren (für die Profis: sortieren nach 'x')
snacks = {
    1: {"name": "Erdnüsse", "price": 200, "amount": 50, "pos": {"x": 10}},
    2: {"name": "Milka", "price": 400, "amount": 20, "pos": {"x": 30}},
    3: {"name": "Snickers", "price": 100, "amount": 10, "pos": {"x": 50}},
}
sorted_snacks = sorted(snacks.items(), key=lambda e: e[1]["price"])
print("*" * 40)
# print(list(snacks.items())[0][1]["price"])
