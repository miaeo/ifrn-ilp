while True:
   n1 = input('Digite o primeiro numero ou pare para terminar: ')
   if n1 == 'pare':
      break
   n2 = int(input('Digite o segundo numero: '))

   assert n2 != 0, 'Valor deve ser maior que zero'

   resultado = int(n1) / n2
   print ('O resultado da divisao é:', resultado)
print ('Fim da execuçao')