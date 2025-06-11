import requests

def buscar_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if resposta.status_code != 200:
        return 'cep inválido'
    else:
        cep_encontrado = resposta.json()
        return cep_encontrado
    
cep = input('informe o cep:')
resultado = buscar_cep(cep)

print(f'Rua: {resultado['logradouro']}')
print(f'Bairro: {resultado['bairro']}')
print(f'Localidade: {resultado['localidade']}')
print(f'Estado: {resultado['estado']}')
print(f'Região: {resultado['regiao']}')