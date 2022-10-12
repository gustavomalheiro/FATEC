print("Grupo 8")
print("Dominickie Peres Ferreira")
print("Gustavo Malheiro")
print("Gustavo Martins Ferrari")
print("Lucas Lessa de Macedo")
print("Questao 1")

Min = int(input("Entre com um numero inteiro maior que 1: "))

while Min <= 1:
    print("Errado! Entre com um numero maior que 1!!")
    Min = int(input("Entre com um numero inteiro maior que 1: "))

Max = int(input("Entre com um numero maior que o Min: "))

while Max <= Min:
    print("Errado! Entre com um numero maior que Min!!")
    Max = int(input("Entre com um numero maior que o Min: "))

print("Min = {} e Max = {}".format(Min, Max))

primo = 0
soma = 0
lista_primos = []

i = Min
j = 1

while i <= Max: 
    j = 1
    primo = 0 
    while j <= Max: 
        if i % j == 0: 
            primo += 1 
        j += 1 
        
    if primo == 2:
        print(i)
        lista_primos.append(i)
        
    i += 1

if lista_primos == []:
   print('Não há primos no intervalo [{}, {}]'.format(Min, Max))
else:
    for x in lista_primos:
        soma += x

    print("Quantidade de primos no intervalo [{}, {}] = {}".format(Min, Max, len(lista_primos)))
    print("Soma dos primos no intervalo [{}, {}] = {}".format(Min, Max, soma))   