
## Funçao que encontra se há um subarray cujo a soma é um valor ímpar
def oddSubArray(array):
  i = 0
  while (i <= len(array)-1):
    j = 0
    while (j <= len(array)):
      if(i < j):
        if((sum(array[i:j]) % 2 != 0) and (j-i != 1)):
          print (array[i:j])
          return True
      else:
        if((sum(array[j:i]) % 2 != 0) and (i-j != 1)):
          print (array[j:i])
          return True
      j += 1
    i += 1
  return False

## Função que verifica se é possível sobrepor os números do array para que a soma do mesmo seja ímpar
## Lógica: Se a soma for par, e houver tanto números pares quanto ímpares, retornará True
def oddify(array):
  if (sum(array)%2 != 0):
    return True
  impar = False
  par = False
  for i in array:
    if (i % 2 == 0):
      par = True
    else:
      impar = True
    if(impar == True and par == True):
      return True
  return False

t = int(input())
while(t > 0):
  n = int(input())
  numArray = input().split(" ")
  numArray = [int(i) for i in numArray]

  if(oddify(numArray)):
    print("YES")
  else:
    print("NO")
  t-=1