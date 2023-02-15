import random

print("******************************")
print("**** Jogo de adivinhação! ****")
print("******************************")

numero_secreto = random.randint(1, 100)
total_de_tentativas = 0
rodada = 1

print("Qual o nível de dificuldade?\n[1]Fácil [2]Médio [3]Difícil")
nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

while(rodada <= total_de_tentativas):
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite o seu número entre 1 e 100: "))

    if(chute < 1 or chute > 100):
        print("Você deve digitar um numero entre 1 e 100")
        print("Você digitou ", chute)
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    elif(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada += 1

print("Fim de Jogo")