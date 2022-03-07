"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de exercícios
Tema: Condicionais
Diversão do carnaval \o/

Exercício 3:
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns
Barulho	Nível sonoro    (dB)
Britadeira	            130
Cortador de grama	      106
Despertador	            70
Cômodo em silêncio	    40

Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho.
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está.
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 

"""

# Definindo o dicionário com as informações da tabela
dic = {
    "Britadeira" : 130,
    "Cortador de grama" : 106,
    "Despertador" : 70,
    "Cômodo em silêncio" : 40
}

# Convertendo chaves do dicionário em lista
dic_keys = list(dic.keys())

# Solicitando entrada de nível sonoro do usuário em decibéis

nivel_sonoro = int(input("Digite o nível sonoro em decibéis: "))

# Verificando se o valor digitado está na tabela
if nivel_sonoro in dic.values():
    for key, value in dic.items():
        if nivel_sonoro == value:
            print(f"\nEsse valor de decibéis corresponde a: {key}")
# Determinando outras condições
elif nivel_sonoro > 130:
    print(f"\nO valor está acima do valor máximo da tabela!")
elif nivel_sonoro > 106:
    print(f"O valor digitado está entre o barulho de um {dic_keys[1]} e uma {dic_keys[0]}")
elif nivel_sonoro >70:
    print(f"O valor digitado está entre o barulho de um {dic_keys[2]} e um {dic_keys[1]}")
elif nivel_sonoro> 40:
    print(f"O valor digitado está entre o barulho de um {dic_keys[3]} e um {dic_keys[2]}")
else:
    print ("O valor é menor que todos os valores da tabela!")
