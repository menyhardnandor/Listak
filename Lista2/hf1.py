import random
paratlan = []

for i in range(1,40):
    szam = random.randint(1,40)
    if szam % 3 == 0:
        paratlan.append(szam)
print(paratlan)
    
