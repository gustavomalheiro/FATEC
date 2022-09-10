"""
Escreva um programa que contenha um laço que será executado enquanto o número digitado for 
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis 
por 2 e por 3.
"""
num = 1

while num != 0:
    num = int(input("Entre com um numero. (Para sair, digite 0): "))

    if num % 2 == 0 and num % 3 == 0:
        print(f"divisivel por 3 E por 2: {num}")
    
