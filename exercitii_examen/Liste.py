# Lista este o structura de date ordonata si mutabila
# Permite elemente duplicat
# Este definita folosind paranteze drepte
# Elementele pot fi accesate folosindu-se un index, fiecare element are un index
# Numerotarea index-ilor incepe de la 0 si se termina la n-1, unde n reprezinta numarul de lemente dintr-o lista
# my_list = [8, 2, 3, 4, 'Ana are mere', True, None]

# Pentru accesarea unui element se va folosi numele listei precedat de indexul dorit scris intre paranteze drepte []
# print(my_list[1])

# Elementele din lista pot fi accesate si de la final spre inceput prin folosirea indexilor negativi
# print(my_list[-3])

# Lungimea unei liste se afla cu ajutorul functiei len()
# print(len(my_list))

# Slice - impartirea listelor
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_sliced_list = my_list[4:]
# my_sliced_list = my_list[-5:]
# my_sliced_list = my_list[:6]
# my_sliced_list = my_list[:-5]
# my_sliced_list = my_list[4:7]
# my_sliced_list = my_list[-5:-2]
# my_sliced_list = my_list[2:-5]
# print(my_sliced_list)

# Slice - definirea pasului

# Folosind toata lista si pas
# my_sliced_list = my_list[::2] - numara toata lista de la inceput din 2 in 2

# Folosind doar index de start si pas
# my_sliced_list = my_list[1::2] - numara de la indexul 1 pana la sfarsit din 2 in 2

# Folosind index de final si pas - [0, 3, 6]
# my_sliced_list = my_list[:7:3]

# Folosind index de start, final si pas - [2, 6]
# my_sliced_list = my_list[2:-3:4]

#print(my_sliced_list)

# Functionalitati ale listelor

# .index(element)  -->  returneaza indexul elementului 'element'
# .append(element_nou)  -->  adauga elementul 'element_nou' la finalul listei
# .insert(index, element_nou)  -->  adauga elementul 'element_nou' pe pozitia index
# .remove(element) - scoate din lista elementul 'element'
# .pop() - scoate din lista ultimul element
# .pop(index) - scoate din lista elementul de pe pozitia index
# .clear() - scoate din lista toate elementele
# .copy() - copiaza lista intr-o alta lista
# .reverse() - construieste lista avand elementele in ordine inversa
# .sort() - sorteaza elementele din lista in ordine crescatoare
# .count(element) - returneaza de cate ori se afla elementul 'element' in lista

# Concatenarea a doua liste

# list_3 = list_1 + list_2
# list_1.extend(list_2) - elementele din lista 2 vor fi adaugate la finalul liste list_1



