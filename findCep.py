import requests

# Entrada de dados
while True:
    find_cep = input('CEP = ').strip()
    while len(find_cep) != 8:
        print('Quantidade de dígitos inválida!')
        find_cep = input('CEP = ').strip()
    break

# Request da API
cep = requests.get(f'https://cep.awesomeapi.com.br/json/{find_cep}')
cep = cep.json()

# Saída dos dados
while True:
    try:
        print(cep['address'])
        print(cep['district'])
        print(cep['city'])
        print(cep['state'])
        break
    except KeyError:
        print('CEP Inválido!')
        break
