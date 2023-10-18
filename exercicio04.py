num = int(input('Digite um número: '))
#Serve apenas para mostrar o valor inputado pelo usuário no terminal
fatorial = num

#Serve para guardar o valor da multiplicação anterior
result = 1

#Enquanto o valor inputado pelo usuário for maior que zero ele 
# irá realizar o calculo do fatorial subtraindo 1 de num 
while num > 0:
  result *= num
  num -= 1

print("O fatorial de ",num," é ",result)