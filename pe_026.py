n_max = 1
l_max = 1

# 1%n liefert immer 1 für n>1.
# Durch Verzehnfachung (10^x) wird jeweils die nächste Dezimalstelle betrachtet.
# Wenn (10^x)%n wieder 1 ausgibt, ist eine Periode der Nachkommastellen durchgelaufen.
# Jetzt wird x nicht noch einmal erhöht, sondern der Wert der letzten Schleife ausgegeben.

for nenner in range(3, 1000, 2):
    p = 1
    if nenner%5 == 0: continue
    while (10**p)%nenner != 1:
        p += 1
    if p > l_max: n_max, l_max = nenner, p
print(l_max)
