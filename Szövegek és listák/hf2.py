mondat = None
lista = []

while mondat != '':
    mondat = input('Mondj egy mondatot: ')
    
    if mondat == '':
        print('')
    
    elif mondat[-1] == '.':
        lista.append(mondat + '   Kijelentő')
        
    elif mondat[-1] == '?':
        lista.append(mondat + '   Kérdő')
        
    elif mondat[0:8] == 'Bárcsak' or mondat[0:3] == 'Bár' and mondat[-1] == '!':
        lista.append(mondat + '   Óhajtó')
        
    
    elif mondat[-1] == '!':
        lista.append(mondat + '   Felszólító vagy Felkiáltó')
        