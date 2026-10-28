def repeats(arr):
    resultado = 0
    lista = arr

    for i in lista:
        if lista.count(i) == 1:
            resultado = resultado + i

    return resultado


def basic_test_cases():
    assert repeats([4,5,7,5,4,8]) == 15
    assert repeats([9, 10, 19, 13, 19, 13]) == 19
    assert repeats([16, 0, 11, 4, 8, 16, 0, 11]) == 12
    assert repeats([5, 17, 18, 11, 13, 18, 11, 13]) == 22
    assert repeats([5, 10, 19, 13, 10, 13]) == 24

    return True

print(basic_test_cases())



