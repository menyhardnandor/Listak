szo = input('Adj meg egy keresztnevet: ')
szavak = []

while szo != '':
    
    
    if szo[0:1] == 'A':
        szavak.append(szo)
        
    elif szo[0:1] == 'a':
        szavak.append(szo)
        
    if szo[0:1] != 'A':
        szo = input('Adj meg egy keresztnevet: ')
        
    elif szo[0:1] != 'a':
        szo = input('Adj meg egy keresztnevet: ')
        
   
print(szavak)