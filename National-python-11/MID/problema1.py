sir = input("Introduceți maxim 10 litere: ")
lungime_sir = len(sir)
nr_vocale = 0

if lungime_sir <= 10:
    for i in range (0,lungime_sir):
        if sir[i] in ['a','e','i','o','u']:
            nr_vocale = nr_vocale + 1
else:
    print("Numarul de caractere introdus este prea mare")

print("Numarul total de vocale este: ", nr_vocale)
