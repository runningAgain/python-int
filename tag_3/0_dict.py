"""
Dict Recap
"""

# Aufgabe: Gebe jeweils den Namen aus
namen = {
    "lists": [
        {"name": "Peter"},
        {"name": "Daniel"},
        {"name": "Abdelrahman"},
    ]
}

# Peter
# Daniel
# Abdelrahman

print(type(namen))
print(type(namen["lists"]))
# über die Liste mit den Dict-Einträgen iterieren
for entry in namen["lists"]:
    print(entry["name"])


# Aufgabe: Gib den Namen jeder VM aus.
virtualisierung = {
    "cluster": [
        {
            "vms": [
                {"name": "web01"},
                {"name": "db01"},
                {"name": "backup01"},
            ]
        }
    ]
}

# web01
# db01
# backup01
print(type(virtualisierung))
print(type(virtualisierung["cluster"]))  # <class 'list'>
print(type(virtualisierung["cluster"][0]))  # <class 'dict'>

for e in virtualisierung["cluster"][0]["vms"]:
    print(e["name"])
