"""
Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N, 
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse 
requisito)
"""

N = 0
total, i = 0, 1

while N < 100:
    N = int(input("Entre com um numero N maior ou igual a 100: "))
    
    if N < 100:
        print("NO MINIMO 100!")

while i <= N:
    if i % 2 == 0:
        total += i

    i += 1

print(total)



