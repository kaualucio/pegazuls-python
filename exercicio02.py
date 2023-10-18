
firstValue = 0
secondValue = 1
sumFirstAndSecond = 0

# Para iteração do while
i = 0

#Primeiro printa os dois primeiros números necessários para a sequência acontecer
print(firstValue)
print(secondValue)

# Por já ter printado os 2 primeiros números pedi para o 
# while printar os próximos 18 números da sequência
while i < 18:
  #Soma o primeiro e segundo valor
  sumFirstAndSecond = firstValue + secondValue
  print(sumFirstAndSecond)

  #Após a soma o segundo valor passa a ser o primeiro e 
  # a soma dos dois números anteriores passa a ser o segundo
  firstValue = secondValue
  secondValue = sumFirstAndSecond

  #Acrescenta mais um ao contador
  i += 1