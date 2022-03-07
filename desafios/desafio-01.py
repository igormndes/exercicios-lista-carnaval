"""
How Bootcamps - Stone - /código[s]
Data: 07/03/2022
Autor: Igor Gabryell Mendes Melo
Descrição: Exercicio proposto pelo instrutor Henrique Branco.
Lista de desafios
Diversão do carnaval \o/

Desafio 1:

Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

⦁	O jogo deve sortear um número entre 1 e 100.
⦁	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100.
⦁   Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
⦁	O número do usuário deve ser analisado:
⦁	Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
⦁	Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
⦁	Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado,
    sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
⦁	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. Caso contrário, o jogo deve ser encerrado.

"""
from random import random, randrange

resposta = (input("\nVocê está pronto para jogar? Se estiver digite 'sim'\n")).upper()

while resposta == "SIM":
    # Gerando um número de forma aleatória
    numero_sorteado = randrange(0, 101)

    # Número de tentativas
    total_de_tentativas = 0

    # Nível de dificuldade
    print("Escolha o nível de dificuldade: ")
    print("(1) Fácil (2)Médio (3)Difícil\n")

    nivel = int(input("Escolha o nível de dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 10
    elif (nivel == 2):
        total_de_tentativas = 6
    elif (nivel == 3):
        total_de_tentativas = 3
    elif (nivel < 1 or nivel > 3):
        print("\nVocê conseguiu perder sem jogar!\n")

    for tentativas in range(1, total_de_tentativas + 1):
        print(f"Tentativa {tentativas} de {total_de_tentativas}\n")

        numero_escolhido = int(input("Digite um número inteiro entre 0 e 100: "))

        if (numero_escolhido < 0 or numero_escolhido > 101):
            print("Você deve digitar um número inteiro entre 0 e 100!")
            continue

        acertou = numero_escolhido == numero_sorteado
        maior = numero_escolhido > numero_sorteado
        menor = numero_escolhido < numero_sorteado

        if (acertou):
            print("Parabéns! Você acertou o número da sorte!\n")
            break
        elif (maior):
            print("Você errou! O número escolhido é maior que o número da sorte!\n")
        elif (menor):
            print("Você errou! O número escolhido é menor que o número da sorte!\n")

    resposta= input("Você deseja jogar novamente?").upper()

print ("\nFim de jogo. Obrigado!\n")
