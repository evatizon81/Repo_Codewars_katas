def camel_case(texto):
    palabra_limpia = texto.replace('-','_')
    palabra_limpia = palabra_limpia.split('_')
    primera_palabra = palabra_limpia[0]
    resto_palabra = palabra_limpia[1:]
    primera = ""
    lista_aux = []


    for i in resto_palabra:
        aux = i.lower() 
        aux = aux[0].upper() + aux[1:]
        lista_aux.append(aux)

    if primera_palabra[0].isupper():
        primera = primera_palabra.lower()
        primera = primera[0].upper() + primera[1:]
    else:
        primera = primera_palabra.lower()

    palabra_completa = primera + "".join(lista_aux)

    return palabra_completa


print(camel_case("The_Stealth-Warrior"))
    

