# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# Nome de classe: primeira letra de cada palavra com letra maiúscula
# class Aluno:
# class Aluno():
class Aluno(object):    # Três formas equivalentes de criar a classe.
    def __init__(self, nome, mensalidade, idade):  # Método construtor
        self.nome = nome                # Atributos
        self.mensalidade = mensalidade  # self.nome_atributo = parametro
        self.idade = idade
    def get_nome(self):                 # Métodos gets (consulta)
        return self.nome
    def get_mensalidade(self):          # Consulta o valor do atributo e retorna
        return self.mensalidade
    def get_idade(self):
        return self.idade
    def set_nome(self, novo_nome):      # Métodos sets (altera)
        self.nome = novo_nome
    def set_mensalidade(self, nova_mensalidade): # Altera o valor do atributo e não retorna
        self.mensalidade = nova_mensalidade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def aumento_mensalidade_valor(self, valor_aumento):     # Solução 1
        self.mensalidade = self.mensalidade + valor_aumento
        # self.mensalidade += valor_aumento
    def pode_cnh(self):
        if self.idade >= 18:
            print("Pode CNH.")
        else:
            print("Não pode CNH.")


if __name__ == '__main__':                # Atalho: mai <tab>
    aluno1 = Aluno('Paulo', 1100.00, 21)  # Chama o método __init__ (construtor)
    print(aluno1)  # Mostra o endereço hexadecimal onde o objeto foi armazenado
    # <aluno.Aluno object at 0x000001F5FB466D50>
    aluno2 = Aluno('Emily', 1300.00, 17)  # Chama o método __init__ (construtor)
    print(aluno2)  # Mostra o objeto da classe Aluno e o endereço hexadecimal
    # <aluno.Aluno object at 0x000001F5FB466D20>
    print("- Aluno 1:\nNome:", aluno1.get_nome())  # print(nome_objeto.nome_metodo())
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:", aluno1.get_idade())
    print("- Aluno 2:\nNome:", aluno2.get_nome())  # print(nome_objeto.nome_metodo())
    print(f"Mensalidade: {aluno2.get_mensalidade()}")
    print(f'Idade: {aluno2.get_idade()}')
    # nome1 = "Ailton Pinheiro"
    nome1 = input("Novo nome: ")                        # Solução 1
    aluno1.set_nome(nome1)  # nome_objeto.nome_metodo() - não retorna dado
    # aluno1.set_nome(input("Novo nome: "))  # Equivalente as 2 linhas anteriores
    print('Nome atualizado:', aluno1.get_nome())        # Verifica (testa)
    aluno2.set_nome("Alice")                            # Solução 2
    print('Nome atualizado:', aluno2.get_nome())        # Verifica (testa)
    aluno1.set_mensalidade(1200.00)
    print("Mensalidade atualizada:", aluno1.get_mensalidade())  # Verifica (testa)

    aluno1.aumento_mensalidade_valor(111)
    print('Mensalidade com aumento:', aluno1.get_mensalidade()) # Verificação (teste)
    aluno2.aumento_mensalidade_valor(155)
    print('Mensalidade com aumento:', aluno2.get_mensalidade()) # Verificação (teste)
    aluno1.pode_cnh()
    aluno2.pode_cnh()
