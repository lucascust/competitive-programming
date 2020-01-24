t = int(input())
while(t > 0):
    sum = 0
    # Valor do maior numero
    max = 0
    # índice do maior dos 3 numeros
    maxindex = -1
    i = 0
    # [a, b, c, n]
    coins = input().split(" ")
    coins = [int(i) for i in coins]
    # pego as moedas e salvo indice e o maximo
    while(i < len(coins)-1):
        sum += coins[i]
        if(coins[i] > max):
            max = coins[i]
            maxindex = i
        i += 1
    # Tiro o ultimo valor da lista e deixo só a lista com "a", "b", "c"
    n = coins.pop()
    # Adiciono o "n" na soma, que é a quarta pessoa que dá as moedas
    sum += n
    # Cálculo de moedas mínimas que a quarta pessoa precisa para repassar
    minVal = (max - coins[maxindex-1]) + (max - coins[maxindex-2])

    # A soma de todas as moedas precisa ser divisível por 3
    # Precisa ser maior que zero para previnir de ninguem ter moeda
    if ((round(sum % 3) == 0) and sum > 0):
        # Aqui dentro já é possivel dividir as moedas, daí basta
        # a quarta pessoa ter moedas suficientes para distribuir
        if(n >= minVal):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1
