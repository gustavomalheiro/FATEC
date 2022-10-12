print("Grupo 8")
print("Dominickie Peres Ferreira")
print("Gustavo Malheiro")
print("Gustavo Martins Ferrari")
print("Lucas Lessa de Macedo")
print("Questao 3")

lista = []

while True:
    N = int(input("Entre com um inteiro N, obrigatoriamente par e maior ou igual a 6 e menor igual a 32: "))

    if N % 2 == 0 and N >= 6 and N <= 32:
        break
    else:
        print("O numero {} é inválido.".format(N))

i = 1
j = 0
lista = []

metade_n = int(N / 2) - 1  # 3
j = int(metade_n / 2)

while i <= metade_n:  # 1 <= 3 / 2 <= 3 / 3 <= 3
    
    if i == 3:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i - 1) * " ") + "**")
    elif i == 4:
        print((int(metade_n - (i - 1)) * " ") + "**" + (i * " ") + "**")
    elif i == 5:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 1) * " ") + "**")
    elif i == 6:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 2) * " ") + "**")
    elif i == 7:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 3) * " ") + "**")
    elif i == 8:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 4) * " ") + "**")
    elif i == 9:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 5) * " ") + "**")
    elif i == 10:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 6) * " ") + "**")
    elif i == 11:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 7) * " ") + "**")
    elif i == 12:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 8) * " ") + "**")
    elif i == 13:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 9) * " ") + "**")
    elif i == 14:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 10) * " ") + "**")
    elif i == 15:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 11) * " ") + "**")
    elif i == 16:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 12) * " ") + "**")
    else:
        # 2 * " " + ** / 1 * " " + **** / 0 + ******
        print((int(metade_n - (i - 1)) * " ") + ("**" * i))
    i += 1  # i = 2 / i = 3 / i = 4


# antes era 2, 4, 6 agora tem que ser 6, 4, 2
while i >= 1:
    
    if i == 3:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i - 1) * " ") + "**")
    elif i == 4:
        print((int(metade_n - (i - 1)) * " ") + "**" + (i * " ") + "**")
    elif i == 5:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 1) * " ") + "**")
    elif i == 6:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 2) * " ") + "**")
    elif i == 7:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 3) * " ") + "**")
    elif i == 8:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 4) * " ") + "**")
    elif i == 9:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 5) * " ") + "**")
    elif i == 10:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 6) * " ") + "**")
    elif i == 11:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 7) * " ") + "**")
    elif i == 12:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 8) * " ") + "**")
    elif i == 13:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 9) * " ") + "**")
    elif i == 14:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 10) * " ") + "**")
    elif i == 15:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 11) * " ") + "**")
    elif i == 16:
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + 12) * " ") + "**")
    else:
        print((int(metade_n - (i - 1)) * " ") + ("**" * i))
    i -= 1


#print((int(metade_n - (i - 1)) * " ") + "**" + () + "**")
