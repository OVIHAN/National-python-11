#   String  -->  "" sau ''  #
my_message = "Ana are mere"
print(my_message)


#   Escaping    #

#   \n   sau   """ """   --> new line - pentru mai multe linii, fraze
#   \   --> new line - pentru o singura linie noua
print('Somnoroase pasarele \nPe la cuiburi se aduna')
print("""Somnoroase pasarele
Pe la cuiburi se aduna
Se ascund in ramurele - 
Noapte buna!""")

#   Formating   #

#   metoda format() - definirea placeholderului se face între acolade { }
print("For only {price:.2f} dollars! {cheers_msg}".format(price = 49, cheers_msg = "Have a great day!"))

#   F - strings
print(f'For only {49:.2f} dollars! {"Have a great day!"}')

