# Gerenciamento de Conjuntos de Dados:
clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}

'''set ou conjunto: é uma coleção desordenada e não indexada de elementos únicos.
Suporta operações matemáticas como união (union()), intersecção(intersection()) e diferença (symmetric_difference()), 
porém o código a seguir utilizará apenas loops com `for`e ìf`. '''

# A. Identificar os clientes que estão em ambos os conjuntos
clientes_em_ambos = set()
for cliente in clientes_A:
    if cliente in clientes_B:
        clientes_em_ambos.add(cliente)

# B. Identificar os clientes que estão apenas em clientes_A
clientes_apenas_A = set()
for cliente in clientes_A:
    if cliente not in clientes_B:
        clientes_apenas_A.add(cliente)

# C. Identificar os clientes que estão em apenas um dos conjuntos
'''add(cliente) é uma função do Python que pertence aos conjuntos (sets). 
A função add é usada para adicionar um único elemento ao conjunto. 
Se o elemento já estiver presente no conjunto, ele não será adicionado novamente, 
garantindo que o conjunto contenha apenas elementos únicos.'''
clientes_apenas_um = set()
for cliente in clientes_A:
    if cliente not in clientes_B:
        clientes_apenas_um.add(cliente)
for cliente in clientes_B:
    if cliente not in clientes_A:
        clientes_apenas_um.add(cliente)

# D. Calcular a porcentagem de clientes únicos
todos_clientes = set()
for cliente in clientes_A:
    todos_clientes.add(cliente)
for cliente in clientes_B:
    todos_clientes.add(cliente)

total_clientes = len(todos_clientes)
clientes_unicos = len(clientes_apenas_um)
percentual_unicos = (clientes_unicos / total_clientes) * 100
'''Função len(): retorna a quantidade de clientes únicos'''

# Exibir resultados
print(f"Clientes em ambos os conjuntos: {clientes_em_ambos}")
print(f"Clientes apenas em clientes_A: {clientes_apenas_A}")
print(f"Clientes em apenas um dos conjuntos: {clientes_apenas_um}")
print(f"Porcentagem de clientes únicos: {percentual_unicos:.2f}")
