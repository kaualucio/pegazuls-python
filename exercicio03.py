#Verifica se o valor no array é unico
# Retorna true se for e false se não for
def checkIfIsUnique(value, arr):
  isUnique = True
  repetition = 0
  i = 0
  while i < len(arr):
    if(arr[i] == value):
      repetition += 1
    
    if(repetition > 1):
      isUnique = False
      break
  
    i+=1

  return isUnique


arrValues = []

#Começa pedindo para o usuário inserir um número
value = int(input('Adicione um número a lista: '))
#Adicionar o primeiro valor ao array
arrValues.append(value)
#E pergunta se quer inserir outro valor
#Caso verdadeiro começa o loop
addAnother = input('Quer adicionar outro valor? [S/N]: ')

while addAnother == 'S' or addAnother == 's':
  value = int(input('Adicione um número a lista: '))
  arrValues.append(value)
  addAnother = input('Quer adicionar outro valor? [S/N]: ')

#Após responder que quer parar de inserir valores na lista 
#Começa a imprimir os valores únicos
for uniqueValue in arrValues:
  isUnique = checkIfIsUnique(uniqueValue, arrValues)
  if(isUnique == True):
    print(uniqueValue)
