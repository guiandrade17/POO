ct = 0              # Valor inicial da variável
print('Digite [-1] para sair da repetição')
while True:  # Laço de repetição, repete enquanto condição verdadeira
    numero = int(input("Digite um número: "))  # Indentação obritória
    if numero == -1:
        break       # Sai de uma estrutura de repetição (while)
    ct = ct + 1     # ct += 1 (contador)
