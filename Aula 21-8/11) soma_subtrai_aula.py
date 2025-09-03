def soma(a, b):       # Recebe dois parãmetros (valoes)
    somar = a + b     # Com a variável local somar
    return somar      # Retorna o resultado do cálculo para o main

def subtrai(a, b):
    return a - b      # Sem variável local

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':             # Atalho: mai <tab>
    num1 = int(input("Primeiro valor inteiro: "))  # Lê os valores
    num2 = int(input("Segundo valor inteiro: "))
    retorno_soma = soma(num1, num2)     # Chama def com variável
    # A variável retorno_soma recebe o valor retornado pela função
    print("Soma =", retorno_soma)
    retorno_subtrai = subtrai(num1, num2)  # Chama def com variável
    print("Subtração =", retorno_subtrai)
