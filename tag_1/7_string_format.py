"""
Format String (f-String)
"""
ram = 42.3323
host = "localhost"
# host hat ram
# .2f => formatiert auf 2 Nachkommastellen
result = f"Host {host} hat {ram:.2f} RAM"
print(result)

print(f"Der Computer {host} steht in Raum 7 und hat {ram} RAM")


# Replace: Entferne x und _ aus user_input
user_input = "_xx23223"
user_input_cleaned = user_input.replace("x", "").replace("_", "")
print(f"der bereinigte Userinput ist: {user_input_cleaned}")

