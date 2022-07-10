lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista.sort()
print('lista ordonata crescator: ' ,lista)
lista.reverse()
print('lista ordonata descrescator: ' ,lista)
lista.sort()
lista_pare = lista[1::2]
print('lista numere pare: ' ,lista_pare)
lista_impare = lista[::2]
print('lista numere impare: ' ,lista_impare)
lista_multiplu = lista[2::3]
print('lista multiplu de 3: ' ,lista_multiplu)
