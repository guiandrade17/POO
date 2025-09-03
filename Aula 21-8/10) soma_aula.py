# O def define a função que recebe os dois parâmetros (dois valores) v1 e v2.
def retorna_soma(v1, v2):       # Assinatura da função
    soma = v1 + v2              # A variável soma recebe o resultado do cálculo
    return soma                 # Retorna o valor calculado
    # Fim da funçao

# A função (def) só será executada quando for chamada na função main.
# O if abaixo indica o início da execução do programa principal (main)
if __name__ == '__main__':                   # mai + <tab> (atalho)
    valor1 = int(input('Primeiro valor: '))  # Indentação obrigatória.
    valor2 = int(input('Segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2)  # Chama a função
    # A variável v_retorno recebe o valor retornado pela função (def)
    print("Soma = ", v_retorno)
