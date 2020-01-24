repr(python)

cases = int(input())
casesCount = 0
soma = 0
maxSum = 0

while (casesCount < cases):
    n = int(input())
    cupcakes = input().split(" ")
    cupcakes = list(map(int, cupcakes))

    # Caso específico 0 à n-1
    i = 0
    j = i
    soma = cupcakes[i]
    if (maxSum < soma):
        maxSum = soma
    while (j > 0):
        j -= 1
        soma = soma + cupcakes[j]
        if (maxSum < soma):
            maxSum = soma
    j = i
    soma = cupcakes[i]
    while (j < n-1):
        j += 1
        soma += cupcakes[j]
        if(j == n-1):
            mainSum = soma
        else:
            if (maxSum < soma):
                maxSum = soma

    # Casos intermediários
    i = 1
    while (i < n-1):
        j = i
        soma = cupcakes[i]
        while (j > 0):
            j -= 1
            soma = soma + cupcakes[j]
            if (maxSum < soma):
                maxSum = soma
        j = i
        soma = cupcakes[i]
        while (j < n-1):
            j += 1
            soma += cupcakes[j]
            if (maxSum < soma):
                maxSum = soma
        i += 1

    # Caso específico 2 -  n a 0
    i = n-1
    j = i
    soma = cupcakes[i]
    if (maxSum < soma):
        maxSum = soma
    while (j > 0):
        j -= 1
        soma = soma + cupcakes[j]
        if (j != 0 and maxSum < soma):
            maxSum = soma
            print("max = " + str(maxSum))
            print(j)
    j = i
    soma = cupcakes[i]
    if (maxSum < soma):
        maxSum = soma
    while (j < n-1):
        j += 1
        soma += cupcakes[j]
        if (maxSum < soma):
            maxSum = soma

    if (maxSum >= mainSum):
        print("NO")
    else:
        print("YES")

    casesCount += 1
