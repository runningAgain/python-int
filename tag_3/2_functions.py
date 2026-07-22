"""
Einführung in Funktionen
"""


def hello_world():
    # Beispiel für sehr einfache Funktionen
    print("Hello World")


def say_hello(name, department):
    # 2 Parameter
    print(f"{name} arbeite in {department}")  # Bob, Dev
    name = name[:2]  # verändert NICHT den namen außerhalb der Funktion
    print(name)
    # lokal => innerhalb einer Funktion (Scope)
    print("Lokale Variablen von say_hello:")
    # diese
    print(locals())


hello_world()
say_hello("Bob", "Development")  # 2 Argumente

# Variablen an Funktion übergeben. Das Slicing innerhalb der Funktion
# verändert nicht den name
name = "Bobby"
job = "Admin"
say_hello(name, job)
print("global name:", name)
print("*" * 40)
print("Globale Variablen:")
# for key, value in list(globals().items()):
#     print(key, value)
