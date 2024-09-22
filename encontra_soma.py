def encontra_soma(numeros, n):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if (numeros[i] + numeros[j] >= n and numeros[i] + numeros[j] < n + 0.01):
                print(f"Soma encontrada: {numeros[i]} + {numeros[j]} = {numeros[i] + numeros[j]:.2f}")


# Função para soma de três valores
'''
def encontra_soma(numeros, n):
    comprimento = len(numeros)
    for i in range(comprimento):
        for j in range(i + 1, comprimento):
            for k in range(j + 1, comprimento):
                soma = numeros[i] + numeros[j] + numeros[k]
                if (soma >= n and soma < n + 0.01):
                    print(f"Soma encontrada: {numeros[i]} + {numeros[j]} + {numeros[k]} = {soma:.2f}")
'''

n = 104.14
numeros = [
    25.75, 26.11, 17.9, 20.79, 20.39, 51.47, 22.89, 27.89, 37.4, 19.25, 23.28, 
    121.18, 21.79, 17.84, 21.96, 28.03, 23.25, 37.15, 23.74, 33.84, 52.47, 57.33, 
    22.01, 25.47, 24.7, 26.31, 27.13, 22.41, 20.57, 60.95, 40.3, 17.84, 23.25, 
    100.7, 17.25, 88.35, 38.89, 42.32, 54.43, 94.23, 67.15, 27.31, 52.53, 49.55, 
    55.01, 65.25, 75.6, 29.81, 29.63, 45.45, 21.24, 27.25, 41.73, 34.95
]

encontra_soma(numeros, n)
