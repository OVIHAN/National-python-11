# class PlayerCharacter:
#     membership = True
#     def __init__(self, name='anonymous', age=0):
#         if (age > 18):
#             self.name = name
#             self.age = age
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#
#     @staticmethod(num1 + num2)
#     def adding_things_2(num1, num2):
#         return num1 + num2


# player1 = PlayerCharacter('Tom', 10)


# print(player1.name, player1.age)
# print(player1.run())
# print(player2.name, player2.age)

# print(player1.adding_things(2, 3))


# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def run(self):
#         print('run')
#
#     def speak(self):
#         print(f'my name is {self._name}, and i am {self._age} years old')
#
# player1 = PlayerCharacter('ovidiu', 99)
# print(player1.speak())

class User:
    def sign_in(self):
        print('loged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
wizard1.attack()
archer1.attack()

