"""
Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor 
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo 
usuário, a quantidade de valores, a soma e a média de todos.
"""
num = 1
maior, menor, cont, total = 0, 0, 0, 0.0

while num > 0:

    num = int(input("Entre com um valor positivo inteiro (digitando um numero negativo ou 0, encerra.): "))
    
    if menor == 0 and num > 0:
        menor = num

    if num > maior:
        maior = num
    
    if num < menor and num > 0:
        menor = num
    
    if num > 0:
        cont += 1
        total += num
       
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Quantidade: {cont}")
print(f"Media: {total / cont}")