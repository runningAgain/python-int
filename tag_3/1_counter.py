"""
Zähler
wc
"""

from collections import Counter

sentence = "the brown fox jumps over the lazy   fox fox fox".split()
# Über Sentence iterieren und prüfen, ist word in wc
# wenn ja:
# wc["jumps"] += 1

# wenn nein:
# wc["jumps"] = 1

wc = {}

for word in sentence:
    if word in wc:
        # wc[word] = wc[word] + 1
        wc[word] += 1
    else:
        wc[word] = 1

print("*" * 40)

wc = {}
for word in sentence:
    wc[word] = wc.get(word, 0) + 1

print(wc)

print("*" * 40)

# Counter zählt die Vorkommen in einer Sequenz
c = Counter(sentence)
print(c.most_common(3))
