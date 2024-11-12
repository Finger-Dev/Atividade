# Gerenciamento de Conjuntos de Dados

Este projeto Python gerencia dois conjuntos de dados de clientes: `clientes_A` e `clientes_B`. O programa realiza várias operações para identificar os clientes que estão em ambos os conjuntos, apenas em um dos conjuntos, e calcula a porcentagem de clientes únicos.


## Funcionalidades

- **Identificar Clientes Comuns**: Encontra os clientes que estão em ambos os conjuntos.
- **Identificar Clientes Apenas em `clientes_A`**: Encontra os clientes que estão apenas no conjunto `clientes_A`.
- **Identificar Clientes em Apenas Um dos Conjuntos**: Encontra os clientes que estão em apenas um dos conjuntos.
- **Calcular Porcentagem de Clientes Únicos**: Calcula a porcentagem de clientes que são únicos entre os dois conjuntos.

## Requisitos

- Python 3.x

## Como Usar

1. **Clone ou faça o download deste repositório**:
   ```sh
   git clone https://github.com/Finger-Dev/Atividade.git
   cd Atividade
   ```

2. **Execute o programa**:
   ```sh
   python ConjuntoGerenciamento.py
   ```

3. **Siga as instruções no terminal**:
   - O programa já possui os conjuntos de clientes `clientes_A` e `clientes_B` pré-definidos.
   - O programa exibirá os resultados das operações conforme os conjuntos fornecidos.

## Exemplo de Uso

### Conjuntos de Clientes

```python
clientes_A = {"Alice", "Bob", "Charlie", "David"}
clientes_B = {"Charlie", "David", "Eve", "Frank"}
```

### Saída Esperada

```plaintext
Clientes em ambos os conjuntos: {'David', 'Charlie'}
Clientes apenas em clientes_A: {'Alice', 'Bob'}
Clientes em apenas um dos conjuntos: {'Alice', 'Eve', 'Frank', 'Bob'}
Porcentagem de clientes únicos: 66.67 %
```

## Explicação

1. **Identificação de Clientes Comuns**:
   - Adiciona clientes que estão em ambos os conjuntos a um novo conjunto `clientes_em_ambos`.
   - União dos conjuntos: {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"}
   - Total: 6 clientes

2. **Identificação de Clientes Apenas em `clientes_A`**:
   - Adiciona clientes que estão apenas em `clientes_A` a um novo conjunto `clientes_apenas_A`.

3. **Identificação de Clientes em Apenas Um dos Conjuntos**:
   - Adiciona clientes que estão em apenas um dos conjuntos a um novo conjunto `clientes_apenas_um`.
   - Clientes apenas em clientes_A: {"Alice", "Bob"}
   - Clientes apenas em clientes_B: {"Eve", "Frank"}
   - Total de clientes em apenas um dos conjuntos: {"Alice", "Bob", "Eve", "Frank"}
   - Total: 4 clientes.


4. **Cálculo de Porcentagem de Clientes Únicos**:
   - Adiciona todos os clientes a um novo conjunto `todos_clientes` para calcular o total de clientes únicos.
   - Calcula a porcentagem de clientes únicos.
   - A porcentagem de clientes únicos é calculada dividindo o número de clientes que estão apenas em um dos conjuntos pelo total de clientes únicos e multiplicando por 100.

Fórmula:  `(Clientes em Apenas um dos Conjuntos / Total de Clientes Únicos) * 100` 

Aplicando os valores:  `(46) * 100 = 66.67% `


## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Contato
Para dúvidas ou sugestões, entre em contato através do e-mail fingerdevfinger@gmail.com.
```
