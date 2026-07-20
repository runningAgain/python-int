"""
Bedingte Anweisungen

Falsiness
Python als falsch interpretiert:
0 => Ganzahl 0
0.0 => Float 0.0
"" => leerer String
[] => leere Liste
() => leerer Tupel
{} => leeres Dictionary
None
Folgende Werte, die an die Funktion bool() übergeben werden, werden von 
False => der boolsche Wert False

"""
x = True
y = False
print("Datentyp von x:", type(x)) # bool

city = "Hamburg"
print("bool von city:", bool(city))

value = 0
# WEnn value ungleich 0 ist, ist die Aussage wahr
if value:
    print("value ist ungleich 0")
else:
    print("value ist 0")


apples = 10
if apples > 5:
    print("Apples ist > 5")

# String-Vergleich
if "hamburg" == "hamburg":
    print("Städtenamen sind identisch")

if city == "Hamburg":
    print("city ist hamburg")

# Prüfen, ob apples > 4 und kleiner als 11
if (apples > 4) and (apples < 11):
    print("Wenn apples > 4 und apples < 11")

if apples > 12 or apples == 10:
    print("apples > 12 or apples == 10")
elif apples > 12 or apples == 10:
    print("apples > 12 or apples == 10")
else:
    print("apples zu klein")


# Aufgabe: User soll seine Heimatstadt eingeben
# Wenn die Stadt Nürnberg ist, dann print(<FRÄNKISCHER DIALEKT>
# Wenn die Stadt Köln ist, dann print(<Kölsch>
# ansosnten Pech gehabt
heimatstadt = input("Wo wohnst du:")
if heimatstadt == "Nürnberg":
    print("fränkischer Dialekt")
elif heimatstadt == "Köln":
    print("Kölsch")
elif heimatstadt == "Berlin":
    print("Berliner Kindl")
else:
    print("Deine Stadt:", heimatstadt, "ist nicht in der Liste")