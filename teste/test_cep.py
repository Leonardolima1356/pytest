import pytest
import requests

@pytest.fixture
def consulta_cep():
    resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
    
    if resposta.status_code != 200:
        return 'cep não encontrado'
    else:
        resposta.status_code = 200
        resposta.json()
        
        return resposta.json()
global resposta

def test_cep_nao_encontrado(consulta_cep):
    resposta = consulta_cep
    
    assert not resposta == "cep não encontrado"
    
    assert 'logradouro' in consulta_cep
    assert 'bairro' in consulta_cep
    assert 'localidade' in consulta_cep
    assert 'uf' in consulta_cep
    assert 'regiao' in consulta_cep
    
    print(f'Rua: {consulta_cep['logradouro']}')
    print(f'Bairro: {consulta_cep['bairro']}')
    print(f'Localidade: {consulta_cep['localidade']}')
    print(f'Estado: {consulta_cep['uf']}')
    print(f'Região: {consulta_cep['regiao']}')
    