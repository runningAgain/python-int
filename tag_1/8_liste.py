""" 
Datentyp liste: Sequentiell, und veränderbar
"""
values = [1, 34, 12, 53]
backup = values # hier wird die Referenz auf die Liste kopiert (Pointer)

print(f"Datentyp von values: {type(values)}")
print(f"Länge einer Liste: {len(values)}")

# Prüfen, ob Elemente in einer Liste sind:
# if len(values) > 0:
if values:
    print("Values hat ...")

# Listen sind veränderbar
values[0] = 42
print(values)

values.append(11)
print(values)

# pop liefert das letzte Element und löscht
print("pop:", values.pop())
print("pop backup:", backup)
print(values[1:3]) # Slicing erzeugt eine neue LIste: [34, 12]
print(values) # alte Liste bleibt unangetastet
print(backup)

# Prüfen, ob zwei Objekte auf den selben Speicherbereich referenzieren
if values is backup:
    print("values und backup sind das selbe Objekt")
    print(f"id von values: {hex(id(values))}")
    print(f"id von backup: {hex(id(backup))}")


def fn(a):
    # a verändert auch values von "außen"
    a.append("Hallo")

fn(values)
print(values)

x = 20**30
y = 20**30
x = 2 
y = 3
y = y - 1
print(x is y)