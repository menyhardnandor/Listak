lista = ['majom', 'ma', 'ember', 'pénz']
lista2 = []
for szo in lista:
    szo = szo.upper()
    lista2.append(szo)
    if len(szo) < 3:
        lista2.remove(szo)

print(lista)
print(lista2)