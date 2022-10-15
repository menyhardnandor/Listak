import random
szam = -1
i = 1
lista = []
while not szam <=3 or szam < 0:
    szam = int(input('Adj meg egy számot 1 és 3 között: '))
    
while i <= 10:
    lista.append(random.randint(1,3))
    i = i + 1

print(lista)

while szam in lista:
    lista.remove(szam)
print(lista)
