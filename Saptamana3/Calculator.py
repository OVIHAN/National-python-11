def validare_variabile(variabila):
    while variabila.isdigit() is False:
        variabila = input("Reintrodu numarul: ")
    return int(variabila)


def validare_operator(op):
    while op not in ['+', '-', '*', '/']:
        op = input('Reintrodu operatorul: ')
    return op


def calculator(a, b, c):
    """
    :param a: primul nr
    :param b: al doilea nr
    :param c: operatorul (+, -, *, /)
    :return: calculeaza operatia a doua numere
    """
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    else:
        while b == 0:
            b = validare_variabile(input('Ai incercat sa imparti la 0!, Introdu un numar diferit de 0: '))
        return a / b


primul_numar = validare_variabile(input("Numar: "))
al_doilea_numar = validare_variabile(input("Numar: "))
operator = validare_operator(input('Operator: '))
total = calculator(primul_numar, al_doilea_numar, operator)
print(f"Rezultatul este: {total}")