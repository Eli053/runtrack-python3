# Job 06
def check_positive_negative(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

# Appels de la fonction check_positive_negative avec des paramètres différents
check_positive_negative(7)
check_positive_negative(-3)
check_positive_negative(0)