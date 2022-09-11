# lista = [1,2,3,4,5,6,7,8,9]
# suma_i = 0
# suma_p = 0
# for x in lista:
#     if x%2!=0:
#         suma_i = suma_i + x
#     else:
#         suma_p = suma_p + x
# print("Suma imparelor =",suma_i)
# print("Suma parelor =",suma_p)

my_list = [1, 2, 3, 4, 5, 6, 7]

element_par = []
for i in my_list:
    if i % 2 == 0:
        element_par.append(i)

print(element_par)


