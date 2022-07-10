#Structuri de date
# my_list = [8, 2, 'a', 8, '4']
# print('Mesaj')
# print(type(my_list)) #tipul unei variabile
# print(my_list[2])
# print(my_list[3])
# print(my_list[-1])
# print(len(my_list))
# my_list.append('ANA')
# print(my_list.index(8))
# my_list.insert(7, 'A')
# #print(my_list[2:5])
# #print(my_list[2::3])
# print(my_list[7:8])
# my_list.append(['A', 'B' 3, 'x', [4, 7, 'w']])
# print(my_list[7][7][4][2])

#Tupluri - ordonate / imutabile(nu pot fi modificate)
# my_tuple = (8, 2, 'a', 8, '4')
# zilele_anului = tuple()

#Seturi - neordonate(nu pot fi indexate) / imutabile(nu pot fi modificate)

# set_1 = {'mar', 'para', 'banana'}
# print(set_1)
#
# # Dictionare
#
# my_var = 7
#mesaj = None
# mesaj = "Set instructiuni #2"
# if my_var < 6:
#     mesaj = "Se instructiuni #1"
# else
#     mesaj = "Set instructiuni #2"
# mesaj = "Set instructiuni #1" if my_var < 6 else "Set instructiuni #2"
# if my_var < 6 and (mesaj := "Set instructiuni#1"):
#     print(mesaj)
# print(my_var, mesaj)

# a = 1
# b = 2
# impartire
# # if a > 0 and b > 0 and (impartire := a / b): and impartire > 1:
# if a > 0 and b > 0 and a / b > 1:
#     impartire = a / b
#     print(impartire)
# sir = "Ana are mere"
# sir1 = list(sir)
# print(sir1)
# for i, v in enumerate(sir1):
#     print(i, '=>>', v)
# for variabila_temporara in range(len(sir)):
#     print(variabila_temporara, '=>>', sir[variabila_temporara])
# dictionar = {'1': "val1", "2": "val2", "3":"cal3"}
# print(dictionar["4"])
# print(dictionar.get("4", "val4"))
# dictionar.update({4: "val4"})
# dictionar[6] = "val5"
# for i, v in dictionar.items():
#     # print(i, "=>>", v)
#     index, value = i
#     print(i, index, "=>>", value)
# for i in dictionar:
#     print(i, "=>>", dictionar[i])
# print(dictionar)
