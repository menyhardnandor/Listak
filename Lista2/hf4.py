szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
szam = None
szamok2 = []

for szam in szamok:
    if szam % 3 == 0:
        szamok2.append(szam)
print(szamok2)