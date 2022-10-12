N = 10

i = 1
j = 0
lista = []

metade_n = int(N / 2) - 1  # 3
j = int(metade_n / 2) 
print(j)
k = metade_n

while i <= metade_n:  # 1 <= 5
    """
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
    else:
    """
    if i == k: # 1 == 5
        print((int(metade_n - (i - 1)) * " ") + "**" + ((i + j) * " ") + "**")
        j -= 1
        k -= 1
    else:
        # 2 * " " + ** / 1 * " " + **** / 0 + ******
        print((int(metade_n - (i - 1)) * " ") + ("**" * i))
        i += 1  # i = 2 / i = 3 / i = 4
    
    


# antes era 2, 4, 6 agora tem que ser 6, 4, 2
while i >= 1:
    """
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
    else:
    """
    print((int(metade_n - (i - 1)) * " ") + ("**" * i))
    i -= 1

#print((int(metade_n - (i - 1)) * " ") + "**" + () + "**")
