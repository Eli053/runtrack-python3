# Job 08
def display_type_and_season(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "ete":
            print("artichaut, aubergine, navet")

# Appels de la fonction display_type_and_season avec des paramètres différents
display_type_and_season("fruits", "hiver")
display_type_and_season("fruits", "ete")
display_type_and_season("legume", "hiver")
display_type_and_season("legume", "ete")