def multiTable(multiplicando): 

    tabla_de_multiplicar = ""
    for multiplicador in range (1, 11):
        tabla_de_multiplicar+ = f"{multiplicador} * {multiplicando} = {multiplicador} * {multiplicando}\n"
    return tabla_de_multiplicar[:-1]

print (multiTable(5))