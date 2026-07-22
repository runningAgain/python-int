"""
Lambda Ausdruck: Anonyme Funktionen (häufig genutzt für Sortieraufgaben)
"Wegwerf-Funktionen"

Funktionen sind First class citizens (Funktionale Programmierung: zb. Lisp, Haskell)
Jede Funktion ist ein Objekt (mit Eigentschaften etc.)

lambda x,y: x + y

vs

def f(x, y):
    return x + y
"""

summe = lambda x, y: x + y  # erzeugt ein Funktionsobjekt
print("Summe:", summe(3, 2))


def a(b):
    b()


def do_something():
    print("ich bin do something")


a(do_something)

# print(globals())
# print(type(1))  # Objekt der Klasse <class 'int'>
# print(type(do_something))  # Objekt der Klasse <class 'function'>

# Eigentschaften eines Objekts
# print(dir(do_something))
# print("*" * 40)
# print(dir("test"))
x = [1, 2, 3]
sorted(x, key=lambda e: e)
