class Prajituri:

    variabila = []

    def __init__(self, nume, pret, gramaj):

        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj

        lista = [self.nume, self.pret, self.gramaj]
        Prajituri.variabila.append(lista)

    def afisare_gramaj(self):
        return sorted(self.variabila, key=lambda x: x[2])

    def afisare_pret(self):
        return sorted(self.variabila, key=lambda x: x[1])

    def __str__(self):
        return f"Prajitura este {self.nume}, costa {self.pret} lei si are un gramaj de {self.gramaj}g"


class Tort(Prajituri):

    def __init__(self, nume, pret, gramaj, etajat=False, glazura="ciocolata"):
        super().__init__(nume, pret, gramaj)
        self.etajat = etajat
        self.glazura = glazura

    def __str__(self):
        return f"Tortul este {self.nume}, costa {self.pret} lei si are un gramaj de {self.gramaj}g, Etajarea este {self.etajat} iar glazura este {self.glazura}"


class Fursec(Prajituri):
    pass


obj_1 = Prajituri('Amandina', 2, 200)
obj_2 = Prajituri('Briosa', 3, 300)
obj_3 = Prajituri('Gogoasa', 4, 400)

obiect_1 = Tort("Elena", 10, 100, glazura='vanilie')
obiect_2 = Tort("Ana", 20, 200, True, glazura='capsuni')
obiect_3 = Tort("Ema", 30, 300, True)

print(obj_1)
print(obj_2)
print(obj_3)
print(obj_3.afisare_pret())
print(obj_3.afisare_gramaj())

print(obiect_1)
print(obiect_2)
print(obiect_3)

obiect_1.etajat=True
print(obiect_1)
obiect_1.glazura='cacao'
print(obiect_1)

obj7 = Fursec('Fursec ciocolata', 20, 100)
obj8 = Fursec('Fursec vanilie', 40, 500)
obj9 = Fursec('Fursec capsuni', 60, 300)

print(obj7)
print(obj8)
print(obj9)