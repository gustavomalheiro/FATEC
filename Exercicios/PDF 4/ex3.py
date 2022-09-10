"""
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o 
menor e o maior, apresentando-os na tela.
"""
N = int(input("Entre com um numero inteiro N: "))

i = 0
maior, menor = 0, 0

while i < N:
    real = float(input("Entre com um numero real: "))

    menor = real
    
    if real > maior:
        maior = real
    
    if real < menor:
        menor = real

    i += 1

print(f"Maior: {maior} \nMenor: {menor}")
