mondat = None


while mondat != 'vége':
    mondat = input('Mondj egy mondatot: ')
    
    
    if mondat[-1] == '.':
        print('Kijelentő')
        
    if mondat[-1] == '?':
        print('Kérdő')
        
    if mondat[0:8] == 'Bárcsak' or mondat[0:3] == 'Bár' and mondat[-1] == '!':
        print('Óhajtó')
        
    
    elif mondat[-1] == '!':
        print('Felszólító vagy Felkiáltó')
    
        
    
    
    
    
    
    
    
'''else:
    print('Nem értelmezhető mondat')'''