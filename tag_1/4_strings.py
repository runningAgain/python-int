""" 
Datentyp String: unveränderlicher, sequentieller Datentyp.
"""

string = "Spam"
string2 = 'Spam'
print(type(string))
print("Zeichen an Index 0", string[0])               # S
print("letzte Zeichen eines Strings", string[-1])    # m
print("vorletzte Zeichen eines Strings", string[-2]) # a
# Strings sind unveränderlich, man kann sie nicht ändern
# string[0] = "P" TypeError: 'str' object does not support item assignment
x = 99 
y = 12
print(str(x) + str(y)) # 9912


# Länge einer Sequenz
print("Länge des Strings:", len(string))
# Prüfen ob ein STring länger ist als 0
user_input = ""

# klassische Variante
if len(user_input) > 0:
    print("Userinput ist größer als 0")

# pythonische Variante (ist wahr, wenn der String > 0 Zeichen hat)
if user_input:
    print("Userinput ist größer als 0")