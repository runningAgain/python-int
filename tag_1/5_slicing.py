"""
Die Slice-Notation (Substrings)
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""
a = "Hamburg"
b = a
print(a[0:4])  # erzeugt einen neuen STring

url = "www.web.de" # www.web
url_path = url[0:7]
print("Url path:", url_path)

print(url[0:-1]) # www.web.d
print(url[:-1]) # www.web.d

"""
# Übung
# Schneide jeweils alle A aus den Strings
AAAAB => AAAA
BBAAABBB => AAA
"""
s1 = "AAAAB"
# AAAA
print(s1[:-1])

s2 = "BBAAACBBB"
# AAA
print(s2[2:5])


city = "nürnberg"
if "berg" in city:
    print("berg ist in nürnberg")



"""
Aufgabe:
Ein Wort soll auf Gültigkeit geprüft werden.

Gib ein Wort ein und überprüfe anschließend folgende Regeln:

1. Das Wort darf keine Leerzeichen enthalten. (in), zb. mit: " " not in
2. Der Buchstabe "A" darf nicht an der ersten Stelle stehen.
3. Das Wort muss mindestens 3 Zeichen lang sein. (len >= 3)

Ist mindestens eine Regel verletzt, gib aus:
Ihre Eingabe war: <Eingabe>
Ihre Eingabe ist leider falsch.

Andernfalls gib aus:
Ihre Eingabe ist korrekt.
"""

x = " abcde"

word = "Hello_World"
if " " not in word and word[0] != "A" and len(word) >= 3:
    print("Das Wort ist richtig")

