szo = None
szavak = []

while szo != '':
    szo = input('Adj meg egy keresztnevet: ')
    if szo[0:1] != 'a':
        szo = input('Adj meg egy keresztnevet: ')
    if szo[0:1] == 'a':
        szavak.append(szo)
print(szavak)