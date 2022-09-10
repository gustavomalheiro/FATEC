N = int(input("Entre com o numero de termos: "))
Prim = int(input("Entre com o numero Prim: "))

i, aux, fibo, anterior = 1, 0, (Prim + 1), Prim

while i < N: 

    if i == 1:
        print(fibo)

    aux = fibo 
    fibo = fibo + anterior 
    anterior = aux 

    print(fibo) 

    i += 1

# comeca em 1, pois a primeira iteracao do laco printa 2 resultados
# sendo assim, so e necessario printar mais N - 2 vezes