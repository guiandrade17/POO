# o def define a função que recebe dois parâmetros (dois valores)
def maximo(num1, num2):         # Assinatura da função
    if num1 > num2:             # Se numero1 for maior que numero2
        maior = num1
    else:
        maior = num2
    return maior                # Retorna o maior valor

# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':      # Atalho: mai <tab>
    numero1 = int(input("Primeiro número: "))
    numero2 = int(input("Segundo número: "))
    vl_retorno = maximo(numero1, numero2)
    # A variável vl_retorno recebe o valor retornado pela função
    print("\nMaior valor:", vl_retorno)
