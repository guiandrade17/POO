primeiro = int(input("Primeiro valor: "))
ultimo = int(input("Último valor: "))
print("- Sequência de números inteiros:")   # Cabeçalho.
for numero in range(primeiro, ultimo+1, 1):
    print(numero)
print('\nEncerrou a repetição.')
