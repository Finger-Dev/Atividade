def imprimir_piramide(n, crescente=True):
    for i in range(1, n + 1):
        # Imprime os espaços em branco
        print(' ' * (n - i), end='')

        if crescente:
            # Imprime os números em ordem crescente
            for j in range(1, i + 1):
                print(j, end=' ')
        else:
            # Imprime os números em ordem decrescente
            for _ in range(i):
                print(i, end=' ')
        
        print()  # Nova linha após cada nível da pirâmide

try:
    num = int(input("Digite um número inteiro: "))
    if num < 1:
        print("Favor digitar um número válido (maior ou igual a 1): ")
    else:
        imprimir_piramide(num, crescente=True)  # Alterne para False se desejar a pirâmide decrescente
except ValueError:
    print("Entrada inválida. Favor inserir um número inteiro válido.")
