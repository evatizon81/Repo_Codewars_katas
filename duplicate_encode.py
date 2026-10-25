def duplicate_encode (word):

    palabra = word.lower()
    resultado = ""

    for i in palabra:
        aux = palabra.count(i)
        if aux == 1:
            resultado = resultado + '('
        else: 
            resultado = resultado + ')'
            

    return resultado


print(duplicate_encode("aaaaaaaata"))
            
  