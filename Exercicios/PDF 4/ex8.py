num = int(input("Entre com um numero inteiro: ")) 

i = 1
primo = 0

while i <= num: 
    if num % i == 0: 
        primo += 1 
    i += 1

if primo <= 2: 
    print("É primo.")
else:
    print("Nao é primo.")