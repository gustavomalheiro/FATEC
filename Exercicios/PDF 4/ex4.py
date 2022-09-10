"""
Reescreva um programa do exercício acima considerando exclusivamente os números positivos 
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem 
"número inválido" e o valor deve ser ignorado.
"""
N = int(input("Entre com um numero inteiro N: "))

i = 0
maior, menor = 0, 0

while i < N:
    real = float(input("Entre com um numero real: "))
    
    if real <= 0:
        print("Numero invalido")
    else:
        if menor == 0:
            menor = real
        
        if real > maior:
            maior = real
        
        if real < menor:
            menor = real
        
        i += 1
    
print(f"Maior: {maior} \nMenor: {menor}")
