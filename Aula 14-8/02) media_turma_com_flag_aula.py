ct = 0                  # Valor inicial das variáveis
soma = 0
print('Digite [-1] para sair')
while True:  # Laço de repetição while, repete enquanto condição verdadeira
    nota = float(input("Nota do aluno: "))  # Indentação é obritória
    if nota == -1:
        break           # Sai de uma estrutura de repetição (while)
    ct = ct + 1         # ct += 1 (contador), incrementa o ct
    soma = soma + nota  # soma += nota (somador ou acumulador)
    # Fim da estrutura de repetição "while"
media = soma / ct       # Os comandos voltam para coluna 1
print("Média da turma:", media)
print('Quantidade de alunos:', ct)
