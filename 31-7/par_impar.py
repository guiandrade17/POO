- Problema:
- Elabore um programa que verifica se um valor inteiro fornecido pelo
usuário é par ou ímpar.

- Analise o problema e verifique quais são os dados que o usuário precisa
fornecer (digitar) como entrada.

- Passos para a resolução do problema (algoritmo):
Entrada de dados (leia)
Processamento (cálculo)
Testes (se ...)
Saída de dados (escreva)

- Sintaxe do if ... else:
if condicao1:            # A indentação é obrigatória.
    print(“Mensagem 1”)  # Executa, se a condição1 for verdadeira
else:
    print("Mensagem 3")  # Executa, se a condção1 for falso
Obs.: na linha do "else:" nunca colocar uma condição (um teste)

- Operadores aritméticos:
    +       →       soma
    –       →       subtração
    *       →       multiplicação
    /       →       divisão
    //      →       divisão de inteiros (quociente da divisão)
    %       →       módulo (resto da divisão)
    **      →       potenciação
- Obs.: um número é par se ele for divisível por dois, ou seja,
quando dividimos o número por dois e o resto é igual a zero.
- Dica: use o operador módulo (resto da divisão)  %

Teste 1: valor = 7              Saída: "Número ímpar."
Teste 2: valor = 8              Saída: "Número par."            """

valor = int(input("Digite um número: "))  # Recebe um número digitado
resto = valor % 2               # Pega o resto da divisão de dois números.
if resto == 0:  # Verifica se o valor da variável resto = 0, se o número é par
    print("Número par.")        # Indentação (to indent) obrigatória.
else:                           # Caso contrário
    print("Número ímpar.")
''' --- ALTERAÇÕES:
a. Refaça a solução sem usar a variável resto, use somente uma variável.
b. Na tela de saída, acrescente o número digitado e o valor do resto da 
   divisão por 2.  
c. Acrescente, verifique também se o valor fornecido é divisível por cinco. 
    --- DICAS ABAIXO:
valor = int(input("Digita um número: "))                            # a.
if valor % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")             
print("Valor digitado: ", valor)                                    # b.
print("Resto da divisão: ", resto)              .

if valor % 5 == 0:                                                  # c.
    print ("O número é divisível por 5.")
else:
    print ("O número não é divisível por 5.")          
---

    # print("O número {} é ímpar" .format(valor))   
    
'''
