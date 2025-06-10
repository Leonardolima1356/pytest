from funcao import *

def test_tamanho_string():
    assert tamanho_string("Maria") == 5
    assert tamanho_string("") == 0
    assert tamanho_string("A") == 1

def test_calcular_media():
    assert calcular_media([10, 20, 30]) == 20
    assert calcular_media([5]) == 5
    assert calcular_media([]) == 0
    assert calcular_media([0, 0, 0]) == 0

def test_verificar_maior_idade():
    assert verificar_maior_idade(18) is True
    assert verificar_maior_idade(10) is True
    assert verificar_maior_idade(19) is False
    assert verificar_maior_idade(100) is False

def test_eh_positivo():
    assert eh_positivo(10) == 'positivo'
    assert eh_positivo(0) == 'positivo'
    assert eh_positivo(-5) == 'negativo'

def test_status_aluno():
    assert status_aluno(2.9) == 'reprovado'
    assert status_aluno(3) == 'recuperação'
    assert status_aluno(6.9) == 'recuperação'
    assert status_aluno(7) == 'aprovado'
    assert status_aluno(10) == 'aprovado'