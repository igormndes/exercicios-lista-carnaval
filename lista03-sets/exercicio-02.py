"""
How Bootcamps - Stone - /código[s]
Data: 04/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Dicionários e sets
Diversão do carnaval \o/

Exercício 2:
Faça um programa que lê uma sigla de um estado do usuário e imprime na tela o nome completo do estado. Exemplo:

>>> Digite um estado: SP
>>> O nome completo do estado é São Paulo.


"""
# Definindo siglas e estados
estado = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
    }

# Solicitando entrada de dados do usuário
sigla = input(f"Digite a sigla do estado: \n").upper()

# Devolvendo nome do estado
if sigla in estado.keys():
    print (f"O nome completo do estado é: {estado[sigla]}\n")
else:
    print ("Estado não encontrado!")
