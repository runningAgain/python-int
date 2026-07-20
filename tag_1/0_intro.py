"""
Modul-Docstring

Konventionen:
- Variablennamen:
  - Verwenden Sie Kleinbuchstaben und Unterstriche (snake_case).
  - Vermeiden Sie reservierte Schlüsselwörter oder Namen, die leicht mit
    integrierten Funktionen verwechselt werden können (z. B. `list`, `str`).
  - Namen sollten aussagekräftig sein und den Zweck der Variable
    beschreiben.
  - Variablen dürfen nicht mit einer Zahl beginnen.


- Dateinamen:
  - Verwenden Sie ebenfalls snake_case.
  - Namen sollten beschreiben, was das Skript tut oder wofür es gedacht
    ist.
  - Keine Sonderzeichen oder Leerzeichen in Dateinamen verwenden.
  - Modulnamen sollten nicht mit einer Zahl beginnen, wenn sie später
    importiert werden sollen
  
"""
first_name = "Bob"
# 1x = "Alice" produziert einen Syntax-Error
print("Vorname:", first_name, 42, sep=" ") # \n
print("nächste Zeile")
# print("Hello, World")

x = 42 + 832748
print("x:", x)