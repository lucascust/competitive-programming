repr(python)
try:
    while True:
        n = int(input())
        string = input()
        ls = 0
        rs = 0

        for char in string:
            if (char == "L"):
                ls += 1
            if (char == "R"):
                rs += 1
        print(ls + rs + 1)
except EOFError:
    pass
