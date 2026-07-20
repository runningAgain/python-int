""" 
Listen kopieren
"""
v = [1, 3, 4]
u = v # kopiert nur die Referenz!
z = v.copy() # erstellt eine flache Kopie

# Prüfen, ob v und u identisch sind
print("v is u:", v is u)

# Prüfen, ob z und v identisch sind
print("z is v:", z is v)


# Tiefe Kopie (Deep Copy): braucht man, wenn Listen aus veränderlichen Datentypen
# bestehen (oder Teile davon sind)
from copy import deepcopy

M = [
    [1, 2, 3],
    [4, 5, 6]
]
# N = M.copy()   macht nur eine Flache Kopie, vorsicht, kopiert nur die Referenzen!
N = deepcopy(M) # Echtes Backup
M[0][0] = 99

print(M)
print(N)