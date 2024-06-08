##Crie um script Python que, quando executado, leia dois números inteiros e retorne todos os números ímpares existentes entre eles em ordem crescente. 

n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))

if n1 != n2:
    if n1>n2:
        n1, n2 = n2, n1

    impar=""
    n11 = n1
    n22 = n2

    while n11 <= n22:
        if n11 % 2 != 0:
            impar += str(n11) + " "
        n11 += 1

    print('Os números ímpares entre',n1,'e',n2,'são:',impar.strip())

else:
    print('Os números informados são iguais')
