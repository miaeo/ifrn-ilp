#Crie um script Python que simule o sorteio da Mega-Sena. Para isso, devem ser sorteados aleatoriamente 6 números diferentes entre 1 e 50 e impressos na tela em ordem crescente.

from random import randint
sorteio = []
while len(sorteio) < 6:
    num = randint(1, 50)
    if num not in sorteio:
        sorteio.append(num)

sorteio.sort()

print("<<<<<        SORTEIO MEGA-SENA        >>>>>")
print("Os números sorteados foram: ", sorteio)
