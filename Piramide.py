'''Função imprimir_piramide possui dois parâmetos: 'n' e 'crescente'.
n é parâmetro obrigatório que deve ser fornecido quando a função for chamada 
porque representa a quantidade de linhas da pirâmide e 
determinará quantos loops serão necessários para a quantidade de linhas determinadas.'''
def imprimir_piramide(n, crescente=True):
    # Loop externo que controla o número de linhas da pirâmide (de 1 até n)
    for i in range(1, n + 1):
        # Imprime os espaços em branco à esquerda para centralizar a pirâmide.
        print(' ' * (n - i), end='')

        # Verifica se a ordem é crescente
        if crescente:
            # Loop interno para imprimir os números em ordem crescente (de 1 até i)
            for j in range(1, i + 1):
                print(j, end=' ')
        else:
            # Loop interno para imprimir os números em ordem decrescente (repete o valor de i)
            for _ in range(i):
                print(i, end=' ')
        
        print()  # Nova linha após cada nível da pirâmide

# Bloco try-except para tratar entrada do usuário
try:
    # Solicita ao usuário um número inteiro
    num = int(input("Digite um número inteiro: "))
    # Verifica se o número é menor que 1.
    if num < 1:
        # Informa erro se número for menor que 1.
        print("Favor digitar um número válido (maior ou igual a 1): ")
    else:
        # Chama a função imprimir_piramide com o número inserido e aqui determina a ordem crescente.
        imprimir_piramide(num, crescente=True)  # Alterne para False se desejar a pirâmide decrescente
# Controle de erros try-except.
except ValueError:
    print("Entrada inválida. Favor inserir um número inteiro válido.")
