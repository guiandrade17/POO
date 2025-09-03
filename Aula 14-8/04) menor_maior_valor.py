menor = 999999                      # menor = float('inf')
maior = -999999                     # maior = float('-inf')
print('Digite [0] para sair da repetição')
while True:                         # while valor != -1:
    valor = int(input("Digite um valor: "))
    if valor == 0:
        break
    if valor < menor:
        menor = valor   # Se for menor, atualize o valor da variável menor.
    if valor > maior:   # Aqui, não pode usar else
        maior = valor   # Se for maior, atualize o valor da variável maior.
    # Fim da repetição (while)
print("\nMenor valor:", menor)  # Executa uma vez, volta para coluna 1
print("Maior valor:", maior)
