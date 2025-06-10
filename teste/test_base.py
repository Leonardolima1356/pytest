def eh_par(numero):
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'
    
def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b
    
def test_verifica_se_numero_par():
    assert eh_par(5) == 'é impar'
    assert eh_par(6) == 'é par'
    
def verifica_soma_e_subtrair():
    assert somar(5,6) == 11
    assert subtrair(6,5) == 1