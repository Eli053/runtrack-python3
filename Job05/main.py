# Job 05
def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Éviter la division par zéro
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == '%':
        return num1 % num2
    else:
        return "Opérateur non reconnu"

# Appels de la fonction calcule avec des paramètres différents
result_calculation1 = calcule(10, '+', 5)
print(result_calculation1)

result_calculation2 = calcule(8, '*', 3)
print(result_calculation2)
