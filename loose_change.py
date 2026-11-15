#Remember you have a CHANGE dictionary to work with ;)

def change_count(change):

    tipo_moneda = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
    'dollar': 1.00
}
    
    monedas = change.split()
    total = 0

    for i in monedas:
        total = total + tipo_moneda[i]
     

    return f"${total:.2f}"


if __name__ == '__main__':

    assert change_count('dime penny dollar') == '$1.11'
    assert change_count('dime penny nickel') == '$0.16'
    assert change_count('quarter quarter') == '$0.50'
    assert change_count('dollar penny dollar') == '$2.01'
    assert change_count('dollar dollar dollar dollar dollar dollar dollar dollar dollar dollar penny') == '$10.01'

    print("todo correcto")