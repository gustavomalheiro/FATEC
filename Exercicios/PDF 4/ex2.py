"""
Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor 
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o 
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.
"""

num1 = int(input("Entre com o valor minimo (o valor maximo deve ser maior que o minimo): "))
num2 = int(input("Entre com o valor maximo (o valor maximo deve ser maior que o minimo): "))

i = 1

if num1 > num2:
    print("o valor maximo deve ser maior que o minimo!")
else:
    while i <= num2:
        if i % 5 == 0:
            print(i)
        i += 1
