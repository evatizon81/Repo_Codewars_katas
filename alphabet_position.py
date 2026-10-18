
def alphabet_position(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    text = text.lower()

    for letra in text:
        if letra in alphabet:
            posicion = alphabet.find(letra) + 1
            resultado = resultado + str(posicion) + " "

    return resultado.strip()
    