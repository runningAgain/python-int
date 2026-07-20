"""
Datentyp String: Methoden
"""
name = "Bob"
index_of_B = name.index("B")
print("Index:",index_of_B)

url = "www.google.com"
if url.endswith(".com"):
    print("Com-Domain")

if url.startswith("www"):
    print("www Sub-Domain")

number = "213476"
# Prüfen alle drei, ob ein String ein numberischer Wert ist
url.isdigit
url.isnumeric
url.isdecimal

if number.isdigit():
    print("Number könnte in einen INT gecastet werden")

# upper und lower
user_input = "HamBurg"
if user_input.lower() == "hamburg":
    print("Nutzer wohnt in Hamburg")

lowercase_hh = "HAmBurG".lower()

# Einen String splitten (1,2,3,4,5)
csv_string = "1,2,3,4,5"
csv_string = '1,2,3,4,5'
csv_liste = csv_string.split(",")
print("Type von csv_liste:", type(csv_liste), csv_liste)