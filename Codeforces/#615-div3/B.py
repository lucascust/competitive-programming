t = int(input())
while(t > 0):
    isPossible = "YES"
    n = int(input())
    pos = [0, 0]
    i = 0
    boxArray = []
    path = ""
    while(n > 0):
        box = input().split(" ")
        box[0] = int(box[0])
        box[1] = int(box[1])
        boxArray.append(box)
        n -= 1
    boxArray.sort()

    while (i < len(boxArray)):
        if(pos[0] > boxArray[i][0]) or (pos[1] > boxArray[i][1]):
            isPossible = "NO"
            break

        if(pos[0] < boxArray[i][0]):
            while(pos[0] < boxArray[i][0]):
                pos[0] += 1
                path += "R"

        if(pos[1] < boxArray[i][1]):
            while(pos[1] < boxArray[i][1]):
                pos[1] += 1
                path += "U"

        i += 1
    print(isPossible)
    if(isPossible == "YES"):
        print(path)
    t -= 1
