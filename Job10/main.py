# Job 10
def check_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("Veuillez entrer un nombre entier et positif.")

# Appels de la fonction check_pair_impair avec des paramètres différents
check_pair_impair(7)
check_pair_impair(14)
check_pair_impair(21.5)