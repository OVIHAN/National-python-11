# functii lambda - se mai numesc si functii anonime (fara def/ fara nume)

element = lambda x: x * 10 # unde x este argumentul ;i x * 10 este expresia

# def element(x):
#     return x*10

element_2 = lambda x, y: x + y

""" FILTER """

# Program care sa returneze o lista cu nr pare dintr-o lista initiala

# Functia filter - intoarce un obiect al clasei filter (care este defapt un iterator) rezultat
# prin aplicarea unei functii fiecarui element dintr-un obiect (lista, tuplu, set ...etc.)
list_1 = [1, 5, 4, 6, 8, 11, 3, 12]
# list_2 = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_2)

# ex. cu for loop:
# lista_forloop = []
# for i in list_1:
#     if i % 2 == 0:
#         lista_forloop.append(i)
# print(lista_forloop)

# ex. cu functie clasica

# def filtrare(variabila):
#     if variabila % 2 == 0:
#         return True
#     else:
#         return False
#
# filtered = filter(filtrare, list_1)
# print(list(filtered))

""" MAP """
# Functia filter - intoarce un obiect al clasei MAP (care este defapt un iterator) rezultat
# prin aplicarea unei functii fiecarui element dintr-un obiect iterabil(lista, tuplu, set ...etc.)

list_3 = list(map(lambda x: x * 2 == 0, list_1))
# print(list_3)

""" ZIP """
# Functia ZIP preia parametrii iterabili (pot fi 0 sau ma multi parametii) si returneaza un obiect
# al clasei zip (care este defapt un iterator) sub forma de tupluri, formate din grupuri de elemente
# provenite din parametrii initiali
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale

list_with_int = [1, 2, 3, 4]
list_with_str = ['one', 'two,', 'three', 'four']
list_with_decimal = [1.1, 2.2, 3.3, 4.4]
# result = tuple(zip(list_with_int, list_with_str, list_with_decimal))
# result = dict(zip(list_with_int, list_with_str, ))
result = zip(list_with_int, list_with_str)
# print(result)
# result_list = list(result)
# print(result_list)

val_1, val_2 = zip(*result)
# print("val_1 =  ", val_1)
# print("val_2 =  ", val_2)

""" COMPREHENSION LIST """
var = 'comprehension'

# CASE FOR LOOP
list_for_loop = []
for character in var:
    list_for_loop.append(character)
print(list_for_loop)

# CASE FOR LAMBDA
list_map = list(map(lambda x: x, var))
print(list_map)

# CASE COMPREHENSION
list_string = [character for character in var] # expresie pentru item in lista
print(list_string)

numbers_list = [x for x in range(100) if x % 2 ==0 if x % 5 ==0]
print(numbers_list)

obj = ['Par' if i % 2 == 0 else 'Impar' for i in range(10)]
print(obj)

""" COMPREHENSION DICTIONARY """

# my_dict = {1: 'car', 2: 'bike'}

square_dict = dict()
for num in range (1, 11):
    square_dict[num] = num*num
print(square_dict)

square_dict = {num: num*num for num in range (1, 11)}
print(square_dict)
