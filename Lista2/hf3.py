szavak = ['ajtó', 'tojás', 'Ottó','Tamás', 'tép', 'Tesla', 'alma', 'python']
szavak2 = []
szo = None

for szo in szavak:
    if szo[0:1] == 't':
        szavak2.append(szo)    
        
    elif szo[0:1] == 'T':
        szavak2.append(szo)
print(szavak2)
        