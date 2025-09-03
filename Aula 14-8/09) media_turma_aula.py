ct = 0                      # Inicia o contador
soma = 0                    # Inicia o somador
# soma = ct = 0             # Inicia as 2 variáveis com zero na mesma linha
for i in range(1, 5+1, 1):  # for i in range(1, 6):
    nota = float(input("Nota do aluno: "))  # Indentação obrigatória
    ct = ct + 1             # ct += 1 (contador)
    soma = soma + nota      # soma += nota (somador ou acumulador)
    # Fim da estrutura de repetição for
media = soma / ct
print("\nMédia da turma:", media)
