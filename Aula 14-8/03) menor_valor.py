menor_valor = 99999999          # Valor inicial da variável menor_valor
# menor_valor = float('inf')    # O maior valor possível no Python
print('Digite [0] para sair da repetição')  # Executa uma vez, na coluna 1
while True:                     # Passa várias vezes
    valor = int(input("Digite um valor: "))  # Recebe um número, na coluna 4
    if valor == 0:              # Se o valor for igual a zero
        break                   # Saí do while, encerra o laço.
    if valor < menor_valor:
        menor_valor = valor     # Atualiza a variável menor_valor.
    # Fim da estrutura de repetição (while).
print("\nMenor valor =", menor_valor)  # Executa uma vez, volta para coluna 1
