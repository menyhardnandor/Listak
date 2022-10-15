import random
szamok = []
i = 1

while i != 11:
    szam = random.randint(0,50)
    
    if szam % 4 == 0:
        szamok.append(szam)
        
    i = i + 1
    
print(szamok)
    