# num_calls = 0
#
# def exercitiu(x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
#
# print(exercitiu(4))


# x = 1
#
# def f():
#     return x
#
# print(x)
# print(f())

# x = [1, 2, "hello", "world", ["another", "list"]]
# print(len(x[3]))


# x = (1, 2, 3)
# x[1] = 4


# a = [1, 2, 3]
# b = [4, 5]
# print(a+b*3)

# x = [1, 2, 3, 4]
# print(x[-1:])

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2]= 2
# print(x)

# def exercitiu(i):
#     for i in range(i):
#         return i
#
# x = exercitiu(3)
# print(x)

# a = range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)

# def make_account():
#     return {'balance': 0}
#
# def deposit(account, amount):
#     account['balance'] += amount
#     return account['balance']
#
# a = make_account()
# print(deposit(a, 10))

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#
# a = BankAccount()
# b = BankAccount()
# print(a.deposit(100))

# 'foo' + 2

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

# for k in {"x": 1, "y": 2}:
#     print(k)

# print(list("python"))

# def func(*args):
#     return 3 * len(args)
#
# print(func(4, 4, 4))

# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter == 's':
#             continue
#         print('Current letter : ', letter)
#         var = 10
#         return var
# print(exercitiu(20))

# def f(a, list = []):
#     for i in range(a):
#         list.append(i*i)
#     print(list)
#
# f(3)
# f(2, [1, 2, 3])
# f(2)

# list = ['1', '2', '3', '4', '5']
# print(list[12:])

# class ClasaMea:
#     def Met1(self, a):
#         global var1
#         var1 = a
#
# obj = ClasaMea()
# obj.Met1("Salut lume")

# class Test123():
#     def_str_(self):
#         self.x = 77777
#         return str(self.x)

# class x(object):
#     def Ad(self, a, b, c):
#         return self.a + self.b + self.c
#
# obiect1 = x()
# obiect1.Ad(1, 2, 3)

a = int(input('Introduceti primul numar: '))
b = int(input('Introduceti al doilea numar: '))
c = int(input('Introduceti al treilea numar: '))

val1 = (a / b)
val2 = (a / c)
val3 = (b / c)

def impartire(val1, val2, val3):
    if val1 == val2 and val1 == val3 and val2 == val3:
        return 3 * (val1, val2, val3)
    else:
        return("CIUCIU")

print(impartire)

