# class Exemplu:
#
#     def __init__(self, val=1):
#         self.__first = val
#
#     def set_second(self, valoare):
#         self.second = valoare
#         return self.second


# obiect_1 = Exemplu()
# print(obiect_1._Exemplu__first)
# print(obiect_1.set_second(4))

# obiect_2 = Exemplu(2)
# obiect_2.third = 5

# print(obiect_1.__dict__)
# print(obiect_2.__dict__)


# class Exemplu:
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         Exemplu.__counter +=1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1
#             Exemplu.b = 5
#
# obiect_1 = Exemplu(2)
# print(obiect_1.b)
# print(getattr(obiect_1, 'b'))
# print(Exemplu.b)
#
# # print(obiect_1.__dict__)
# print(Exemplu.__dict__)

# print(hasattr(obiect_1, 'a'))
# print(hasattr(obiect_1, 'b'))

# try:
#     print(obiect_1.a)
# except AttributeError:
#     pass
# try:
#     print(obiect_2.b)
# except AttributeError:
#     pass
# obiect_1 = Exemplu()
# obiect_2 = Exemplu(2)
# obiect_3 = Exemplu(4)

# print(obiect_1.__dict__, obiect_1._Exemplu__counter)
# print(obiect_2.__dict__, obiect_2._Exemplu__counter)
# print(obiect_3.__dict__, obiect_3._Exemplu__counter)

# class Vehicule:
#     pass
#
#
#
# class Masini(Vehicule):
#     pass



# class MasinaDeTeren(Masini):
#     pass
#
# vehicul_1 = Vehicule()
# masina_1 = Masini()
# masina_de_teren = MasinaDeTeren()
#
# # print(issubclass(MasinaDeTeren, Vehicule))
# print(isinstance(masina_1, Masini))

# class Exemplu:
#
#     def __init__(self, val):
#         self.val = val
#
#
# ob1 = Exemplu(0)
# ob2 = Exemplu(2)
# ob3 = ob1
# ob3.val += 1
#
# print(ob1 is ob2)
# print(ob2 is ob3)
# print(ob3 is ob1)
# print(ob1.val, ob2.val, ob3.val)

# str1 = 'Ana are mere '
# str2 = 'Ana are mere mari'
# str1 += 'mari'
#
# print(str1 == str2, str1 is str2)


class SuperClasa:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Numele meu este {self.name}'

class SubClasa(SuperClasa):
    def __init__(self, name):
       SuperClasa.__init__(self, name)
       # self.name = name

    # def __str__(self):
    #     return self.name


obiect = SubClasa('Ovidiu')
print(obiect)
