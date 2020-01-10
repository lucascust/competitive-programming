def mmc(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto is not 0:
        resto = a % b
        a = b
        b = resto

    return (num1 * num2) / a