def permute_a_palindrome(entrada):              # entrada es una variable que almacena una palabra String

    palabra_limpia = entrada.replace(" ","")    # limpiamos espacios
    palabra_mayus = palabra_limpia.upper()      # convertimos a mayúsculas
    letras_palabra_no_repetidas = ""            # almacena la palabra sin repeticiones
    letras_impares = 0                          # contador de letras impares

    for letra1 in palabra_mayus:                # recorre la palabra, letra por letra
        if letras_palabra_no_repetidas.find(letra1) == -1:      # verificar que la letra no está en letras_palabra_no_repetidas    
            contador_de_rep = 0                 # contador de repeteciones de cada letra evaluada

            for letra2 in palabra_mayus:        # recorre la misma palabra comparando la letra del 1º bucle con todas las letras del 2º bucle
                if letra1 == letra2:            # compara si las letras son iguales
                    contador_de_rep = contador_de_rep + 1       # si son iguales incrementamos el contador en 1

            if contador_de_rep % 2 != 0:        # comprobamos si es impar, dividiendo entre 2 y que el resto sea diferente de 0
                letras_impares = letras_impares + 1     # como es impar, entonces incrementamos en 1 el contador de letras impares

            letras_palabra_no_repetidas = letras_palabra_no_repetidas + letra1      # incluímos la letra evaluada

    if letras_impares > 1:      # verificamos si el contador de impares es mayor de 1
        return False            # como es mayor de 1, deducimos que no es palíndromo
    
    return True                 # es palíndromo