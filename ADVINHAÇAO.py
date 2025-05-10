import random 
numero_secreto = random.randint (1,10)
tentativas = 0
contagem_tentativas = 0

print("Bem vindo! que tal jogarmos advinhe o número?")
print("Tente advinhar qual o número entre 1 à 10.")


while tentativas != numero_secreto:
    numero = int(input("Digite um número: "))
    contagem_tentativas= contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns! Você acertou o número secreto!!")
        print(f"Você precisou apenas de {contagem_tentativas} vezes")
        break
    elif numero< numero_secreto:
        print("O número secreto é maior que esse!")
    else: 
        print("O número secreto é menor que esse!") 