def calcula_idade(ano_nascimento):  # Recebe o parâmetro (ano de nascimento)
    ano_atual = 2025                    # Ano atual
    idade = ano_atual - ano_nascimento  # Calcula
    return idade                        # Retorna a idade

if __name__ == '__main__':
    # Leitura do ano de nascimento
    ano = int(input("Digite o ano de nascimento: "))
    v_idade = calcula_idade(ano)        # Chamada da função calcula_idade
    print("Idade da pessoa:", v_idade)
