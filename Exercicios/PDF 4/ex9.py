N = int(input("Entre com um numero inteiro: "))

anterior, fibo = 0, 1
i = 0
aux = 0

while i < N: 

    if i <= 1:
        print(i) 
    else:
        aux = fibo 
        fibo = fibo + anterior 
        anterior = aux 

        print(fibo) 

    i += 1
     
