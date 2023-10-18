#Por ser produto de dois número de 3 dígitos i inicia com 100
i = 100
j = 0
#Resultado final do palindromo
palindromoFinal = 0
#Maior palindromo encontrado naquela iteração
palindromoTemporario = 0

while i <= 999:
  j = i
  while j <= 999:
    #Calula o produto de i e j e transforma para string 
    # para ser possível fazer a inversão e verificar se é igual
    valorProduto = str(i * j)
    valorProdutoInverso = valorProduto[::-1]
    #Caso o valor de valorProdutoInverso for igual valorProduto 
    #significa que ele é palindromo
    if valorProduto == valorProdutoInverso:
        palindromoTemporario = int(valorProduto)
          #Se palindromoTemporario for maior que o atual palindromoFinal
          # o palindromoTemporario passa a ser o novo palindromoFinal
        if palindromoTemporario > palindromoFinal:
            palindromoFinal = palindromoTemporario
    j += 1
  i += 1
  
print(palindromoFinal)
