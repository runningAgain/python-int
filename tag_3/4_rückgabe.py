"""
Rückgabe aus einer Funktion

input -> Verarbeitung -> Output
In Python hat jede Funktion einen Rückgabewert (None)
"""


def ist_gerade(zahl):
    """Prüft, ob eine Zahl gerade ist. Wenn ja, return 1, ansonsten 0."""
    if zahl % 2 == 0:
        return 1
    return 0


x = ist_gerade(4)
print(x)


d = {
    "a": 23,
    "b": 43,
}


# Erstelle eine FUnktion get_key mit zwei Parametern: d (dict), key (str)
# wenn der Key im dict enthalten ist, soll der Wert zurückgeben werden (bei Key "a" => 23)
# wenn der Key nicht drin ist, soll None zurückgegeben werden
def get_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None


x = get_key(d, "c")
print(x)
