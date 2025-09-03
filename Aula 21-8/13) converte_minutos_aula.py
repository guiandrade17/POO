def converte_em_minuto(horas, minutos): # Assinatura da função
    """ Converte hh:mm em minutos. """  # docstring
    vl_minutos = horas * 60 + minutos
    return vl_minutos                   # Retorna o valor calculado

# Início do programa principal
if __name__ == '__main__':              # Atalho: mai <tab>
    h = int(input("Horas: "))           # Lê os dados de entrada
    m = int(input("Minutos: "))
    retorno = converte_em_minuto(h, m)  # Chama a função
    print("Horário em minutos:", retorno)
