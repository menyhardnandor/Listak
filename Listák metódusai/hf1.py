lista = ['kék', 'piros', 'sárga', 'lila']
szin = input('Adj meg egy színt: ')
lista2 = []
if szin in lista:
    print(lista.count(szin))
    lista2.append(szin)
    
elif szin not in lista:
    print('nem szerepel')
    
print(lista2)
