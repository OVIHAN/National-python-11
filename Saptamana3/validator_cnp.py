import datetime


def validare(variabila):
    """
    :param variabila: CNP-ul introdus de utilizator de la tastatura
    :return: CNP-ul valid
    """
    while len(variabila) != 13 and variabila.isdigit() is False:
        variabila = input("Reintrodu CNP-ul: ")
    return variabila


def validare_sex(a):
    if int(a[0]) in range(1, 10):
        return True
    return False


def validate_data_nastere(cnp):
    data_nastere = cnp[1:7]
    try:
        datetime.datetime.strptime(data_nastere, '%y%m%d')
        return True
    except Exception:
        return False


def validare_cod_judet(cnp):
    cod_judet = int(cnp[7:9])
    if cod_judet < 47 or cod_judet in [51, 52]:
        return True
    return False


def validare_evidenta_populatie(cnp):
    evidenta_populatie = int(cnp[9:12])
    if evidenta_populatie in range(1, 1000):
        return True
    return False


def validare_cifra_control(cnp):
    lista_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    cnp = list(cnp)
    suma = 0
    for i in range(12):
        suma = suma + lista_control[i] * int(cnp[i])
    if suma % 11 == 10:
        cifra_control = 1
    else: cifra_control = suma % 11
    if int(cnp[12]) == cifra_control:
        return True
    return False


def validator_cnp(cnp):
    """
    :param cnp: cnp-ul introdus de utilizator de la tastatura
    :return: mesaj valid in cazul in care CNP-ul este valid, "Invalid" in cazul in care CNP-ul este invalid
    """
    if cnp and validare_sex(cnp) and validate_data_nastere(cnp) and validare_cod_judet(cnp) and validare_evidenta_populatie(cnp) and validare_cifra_control(cnp):
        return "Valid"
    return "Invalid"


variabila_cnp = validare(input("Introdu CNP-ul: "))
validator = validator_cnp(variabila_cnp)

print(validator)