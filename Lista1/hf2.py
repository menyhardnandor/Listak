szo = None
szavak = []

while len(szavak) != 3:
    szo = input('Adj meg egy keresztnevet: ')
    if szo != '':
        szavak.append(szo)
    if len(szavak) == 3:
        print(szavak)
print('Program vége')
    