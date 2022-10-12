from random import randint

print("Grupo 8")
print("Dominickie Peres Ferreira")
print("Gustavo Malheiro")
print("Gustavo Martins Ferrari")
print("Lucas Lessa de Macedo")
print("Questao 2")

lista_palpites = []
opcao = 0
chute = 0

Min = int(input("Insira o valor minimo do intervalo: "))

while True:
    Max = int(input(
        "Insira o valor maximo do intervalo (pelo menos 100 de distancia do minimo): "))
    if Max < (Min + 100):
        print("Insira um valor com pelo menos 100 numero de distancia do minimo!")
    else:
        break

while True:
    opcao = int(input("Escolha sua opção de jogo:\n1 - o sorteador é o computador e o adivinhador o humano:\n2 - o sorteador é o humano e o adivinhador é o computador\n"))
    
    if opcao != 1 and opcao != 2:
        print("Apenas 1 e 2 sao opcoes!")
    else:
        break

if opcao == 1:
    print("Computador sorteia, humano adivinha!")
    numero_escolhido = randint(Min, Max)

    print("Numero escolhido!")

    while True:
        
        chute = int(input("Tente adivinhar: "))

        if chute > numero_escolhido:
            print("Numero maior que o escolhido!")
            lista_palpites.append(chute)
        elif chute < numero_escolhido:
            print("Numero menor que o escolhido!")
            lista_palpites.append(chute)
        elif chute == numero_escolhido: 
            lista_palpites.append(chute)
            break

    print("Voce conseguiu! O numero e {}!".format(numero_escolhido))

    print("Numero de palpites dados ate acertar: {}".format(len(lista_palpites)))

    print("Palpites dados:")
    for x in lista_palpites:
        print(x)

elif opcao == 2:
    print("Humano sorteia, computador adivinha!")

    numero = int(input("Insira o numero para o computador adivinhar: "))

    chute_pc = randint(Min, Max)

    while True:

        if chute_pc in lista_palpites:
            chute_pc = randint(Min, Max)

        r = int(input("PC chutou: {} (1 - se certo / 2 - se errado): ".format(chute_pc)))

        if r == 1:

            lista_palpites.append(chute_pc)
            break
        else:
            r = int(
                input("Maior ou menor que o numero sorteado? (1 - maior / 2 - menor): "))
            if r == 1:
                Max = chute_pc
                lista_palpites.append(chute_pc)
            else:
                Min = chute_pc
                lista_palpites.append(chute_pc)

        chute_pc = randint(Min, Max)

    print("Voce conseguiu! O numero e {}!".format(numero))

    print("Numero de palpites dados ate acertar: {}".format(len(lista_palpites)))

    print("Palpites dados:")
    for x in lista_palpites:
        print(x)
