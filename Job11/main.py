# Job 11
def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(f"{heures} heures et {minutes_restantes} minutes")

# Appels de la fonction time_to_text avec des paramètres différents
time_to_text(150)
time_to_text(90)