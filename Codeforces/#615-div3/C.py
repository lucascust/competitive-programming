t = int(input())
while(t > 0):
    isPossible = False
    N = int(input())
    n = N
    aux = []
    count = 0
    i = 2
    string = ""
    while (i <= N/2):
        if(n % i == 0):
            n = n/i
            count += 1
            string += str(i) + " "
            aux.append(i)
            if (count == 2):
                if((n in aux) or(n < 2)):
                    isPossible = False
                    break
                else:
                    string += str(int(n))
                    isPossible = True
                    break
        i += 1
    if(isPossible is True):
        print("YES")
        print(string)
    else:
        print("NO")
    t -= 1
