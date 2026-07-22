"""
Seiteneffekte sind Vorgänge in Funktionen, die globale Variablen verändern.
In der Regel will man keine Seiteneffekte.
"""

values = [1, 2, 3, 4]


def print_values(werteliste):
    """Soll werteliste ausdrucken und lokal letzes Element entfernen (pop)"""
    # Verhindern, dass die globale values-Liste verändert wird: Kopie
    werteliste = werteliste.copy()
    werteliste.pop()  # Entfernt das letze Element
    print("id von werteliste:", id(werteliste))
    print(werteliste)


print_values(values)  # Übergabe per Object Reference
print("Values:", values)
print("id von values:", id(values))
