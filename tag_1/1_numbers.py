"""
Python Integer und arithmetische Operatoren

In Python werden Ganzzahlen als Integer bezeichnet und durch den Datentyp
`int` repräsentiert. Arithmetische Operatoren erlauben mathematische
Berechnungen wie Addition, Subtraktion, Multiplikation und Division.
Hierbei sind auch fortgeschrittene Operatoren wie Modulo oder
Exponentialrechnung verfügbar.

Besonderheiten:
- Integer in Python haben keine feste Größenbeschränkung, sondern nur
  eine Speichergrenze durch die verfügbare Hardware.
- Division mit `/` erzeugt immer einen Fließkommawert (float), selbst
  wenn das Ergebnis mathematisch eine Ganzzahl ist.

Arithmetische Operatoren

x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y => Fließkommazahl
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y
x // y  abgerundeter Quotient von x und y*
Operatoren Precedence (Rangfolge)
https://docs.python.org/3/reference/expressions.html#operator-precedence


Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz zurück.
- `max()`: Gibt den größten Wert einer Sequenz zurück.
"""
MAX_LENGTH = 100

x = -23472
print("Typ von x:", type(x)) # x ist ein Objekt der Klasse int

y = 2 
y = 4
print("y^2:", y**2)
print("5 / 2", 5 / 2)   # 2.5
print("4 / 2", 4 / 2)   # 2.0
print("5 // 2", 5 // 2) # 2
print("5 % 2", 5 % 2) # 1


"""
Aufgabe:
Eine Halle ist 17 Meter lang. Ein Baumstamm ist 4 Meter lang.

Berechne, wie viele Baumstämme der Länge nach in die Halle passen
und wie viele Meter übrig bleiben.

Nutze Konstanten und Variablen.

Beispiel:
Es passen in die Halle: 4 Baumstämme
Es sind noch 1 Meter übrig.
"""
HALL_LENGTH = 17
trunk_length = 4
total_trunks = HALL_LENGTH // trunk_length
total_rest = HALL_LENGTH % trunk_length
print("Es passen", total_trunks, "Baumstämme in die Halle. übrig sind", total_rest)

# Konvertieren von Strings nach Integer
print(3 + int("4"))


# Fließkommazahlen
weight = 89.3 
weight = 89,3 # das ist keine Zahl, sondern ein Tuple
print("Datentyp von weight:", type(weight))


"""
Aufgabe:
Ein Server besitzt Arbeitsspeicher.

Gib den gesamten Arbeitsspeicher in GB und den bereits
belegten Arbeitsspeicher in GB ein.

Berechne, wie viel Arbeitsspeicher noch frei ist.

Nutze Variablen, input(), float() und print().

Beispiel:
Bitte geben Sie den gesamten Arbeitsspeicher ein: 64
Bitte geben Sie den belegten Arbeitsspeicher ein: 18.5

Freier Arbeitsspeicher: 45.5 GB
"""
gesamter_arbeitsspeicher = float(
    input("Bitte geben Sie den gesamten Arbeitsspeicher ein: ")
)
belegter_arbeitsspeicher = float(
    input("Bitte geben Sie den belegten Arbeitsspeicher ein: ")
)

freier_arbeitsspeicher = gesamter_arbeitsspeicher - belegter_arbeitsspeicher

print("Freier Arbeitsspeicher:", freier_arbeitsspeicher, "GB")