import math as mt

def profit(cash):
  gain = 0
  while(cash >= 10):
    aux = mt.floor(cash/10)
    gain = gain + aux
    cash = cash + aux - 10*aux

  return gain 
    

t = int(input())

while t > 0:
  burles = int(input())
  spent = burles + profit(burles)

  print(spent)

  t-=1