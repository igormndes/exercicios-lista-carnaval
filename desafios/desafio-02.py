"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de desafios
Diversão do carnaval \o/

Desafio 2:

Implemente um jogo em que o usuário tenha que adivinhar o somatório de dois dados.
⦁	O jogo deve sortear um número para cada dado. Estes números devem variar entre 1 e 6, inclusive. Deve-se calcular a soma dos dois valores.
⦁	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 2 ou superior a 12. Enquanto o usuário informar um número inválido, 
    o jogo deve solicitar a entrada de um novo número.
⦁	O número do usuário deve ser analisado e o resultado da jogada deve ser apresentado na tela:
⦁	Caso o usuário informe um número superior ou inferior à soma dos dados, o jogo deve apresentar a mensagem “Você errou. A soma dos dados é x.
    O valor do primeiro dado é d1 e o do segundo é d2. ”, sendo x o valor da soma, d1 o valor do primeiro dado e d2 o valor do segundo dado.
⦁	Caso o usuário informe um número igual ao valor da soma, o jogo deve apresentar a mensagem “Parabéns! Você acertou a soma dos dados! O valor do primeiro dado é d1 e o do segundo é d2. ”,
    sendo d1 o valor do primeiro dado e d2 o valor do segundo dado
⦁	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

"""

from random import randrange

resposta = input("\nVocê está pronto?\n").upper()

while resposta == "SIM":
    # Jogando os dados
    dado_01 = randrange(1,7)
    dado_02 = randrange(1,7)

    # Somando
    soma = dado_01 + dado_02

    # Rebendo número válido do usuário

    numero = int(input("Informe a somatória dos dois dados: "))

    while (numero < 2 or numero > 12):
        numero = int(input("\nDigite um somatório possível!\n"))

    if numero != soma:
        print(f"\nVocê errou. A soma dos dados é {soma}.\n"
                f"\nO valor do primeiro dado é {dado_01} e do segundo é {dado_02}.\n")
    elif numero == soma:
        print(f"\nParabéns! Você acertou a soma dos dados! O valor do primeiro dado é {dado_01} e o do segundo é {dado_02}.\n")
    resposta = input("Você deseja jogar novamente? \n").upper()

print("Obrigado!")
