#Desafio Colaborativo

#Na aba Editar da seção denominada Código Desafio, desenvolvam um programa que:

#Leia uma frase escrita pelo usuário;
#Verifique se a string é um palíndromo;
#Retorne na tela a seguinte frase: "A frase (texto) tem n caracteres. É um palíndromo?" (True ou False)

#Exemplo:
#O usuário escreve: Socorram me subi no onibus em Marrocos 
#O programa deve retornar: A frase "socorram me subi no onibus em marrocos" tem 32 caracteres. É um palíndromo? True 

#Importante
#Façam o programa da maneira mais simples e elegante possível; 
#Utilizem apenas conceitos e comandos apresentados nos textos e vídeos até esta unidade.

frase = input("Digite uma frase: ")
frase_sem_espacos = frase.replace(' ', '').lower()
eh_palindromo = frase_sem_espacos == frase_sem_espacos[::-1]

print(f'A frase "{frase}" tem {len(frase_sem_espacos)} caracteres. É um palíndromo? {eh_palindromo}')
