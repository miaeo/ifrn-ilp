##Faça um Programa para um caixa eletrônico. 
##O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
##As notas disponíveis serão as de 10, 20 e 50. O valor mínimo fica sendo de 10 reais e o máximo de 600 reais. 
##O programa não deve se preocupar com a quantidade de notas existentes na máquina.

from time import sleep

def saqueDinheiro():
    while True:
        valor = int(input("Valor do saque: R$ "))
        if 10 <= valor <= 600:
            break
    if valor % 10 != 0:
        print("Impossível sacar esse valor nesse caixa com as notas disponíveis!")
        return
    print("IMPRIMINDO...\n")
    sleep(2)
    notas = [50, 20, 10]
    for nota in notas:
        qtd_notas = valor // nota
        valor %= nota
        if qtd_notas > 0:
            sleep(1)
            print(f"{qtd_notas} nota(s) de R${nota},00.")

print("Nesse caixa você pode sacar até R$600,00!\n– Notas disponíveis: R$10, R$20 e R$50 –\n")
saqueDinheiro()
