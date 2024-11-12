

# Pirâmide de Números

Este projeto Python solicita ao usuário um número inteiro \( n \) e imprime uma pirâmide de números até \( n \). A pirâmide pode ser gerada com números em ordem crescente ou decrescente, dependendo do parâmetro fornecido.

## Funcionalidades

- **Entrada do Usuário**: Solicita ao usuário um número inteiro maior ou igual a 1.
- **Pirâmide Crescente**: Imprime uma pirâmide com números em ordem crescente.
- **Pirâmide Decrescente**: Imprime uma pirâmide com números em ordem decrescente.

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
   python Piramide.py
   ```

3. **Siga as instruções no terminal**:
   - Digite um número inteiro maior ou igual a 1.
   - O programa imprimirá a pirâmide de números conforme a entrada fornecida.

## Exemplo de Uso

### Entrada Crescente (Padrão)

- Para `n = 4` e `crescente=True`:
  ```plaintext
     1
    1 2
   1 2 3
  1 2 3 4
  ```

### Entrada Decrescente

Para obter a pirâmide decrescente, altere o parâmetro `crescente` para `False` na chamada da função `imprimir_piramide` no código.

```python
imprimir_piramide(num, crescente=False)
```

- Para `n = 4` e `crescente=False`:
  ```plaintext
     1
    2 2
   3 3 3
  4 4 4 4
  ```
## Explicação

1. **Função `imprimir_piramide(n, crescente=True)`**:
   - Recebe o número de linhas `n` e o parâmetro `crescente` (padrão é `True`).
   - Imprime espaços em branco para centralizar a pirâmide.
   - Dependendo do valor de `crescente`, imprime os números em ordem crescente ou decrescente.

2. **Entrada do Usuário**:
   - Solicita ao usuário que insira um número inteiro.
   - Verifica se a entrada é válida e maior ou igual a 1.
   - Chama a função `imprimir_piramide` para gerar e exibir a pirâmide.

### Função `imprimir_piramide(n, crescente=True)`

#### Estrutura Geral:
A função `imprimir_piramide` recebe dois parâmetros:
- `n`: Número de linhas da pirâmide.
- `crescente`: Booleano que determina se os números devem ser exibidos em ordem crescente (`True`) ou em ordem decrescente (`False`). O valor padrão é `True`.

### Primeiro Loop: `for i in range(1, n + 1):`
Este loop controla o número de linhas da pirâmide e executa de 1 até `n`, incluindo `n`.

- **Variável `i`**: Representa o número atual da linha que está sendo impressa. Vai de 1 até `n`.

#### Imprimindo Espaços em Branco:
```python
print(' ' * (n - i), end='')
```
- **Objetivo**: Imprimir os espaços em branco antes dos números para alinhar a pirâmide centralmente.
- **Explicação**:
  - `n - i`: Calcula o número de espaços em branco necessários para cada linha. À medida que `i` aumenta, o número de espaços diminui.
  - `' ' * (n - i)`: Cria uma string com `n - i` espaços em branco.
  - `end=''`: Impede a quebra de linha após os espaços em branco para que os números sejam impressos na mesma linha.

### Segundo Loop: Números Crescentes ou Decrescentes

#### Se `crescente` for `True`:
```python
for j in range(1, i + 1):
    print(j, end=' ')
```
- **Variável `j`**: Representa o valor numérico que será impresso. Vai de 1 até `i`.
- **Objetivo**: Imprimir os números de 1 até `i` em cada linha.
- **Explicação**:
  - `range(1, i + 1)`: Cria uma sequência de números de 1 até `i` (inclusive).
  - `print(j, end=' ')`: Imprime cada número na sequência, seguido de um espaço, sem quebrar a linha.

#### Se `crescente` for `False`:
```python
for _ in range(i):
    print(i, end=' ')
```
- **Variável `_`**: Uma convenção em Python para indicar que o valor da variável não é usado. Serve apenas como contador.
- **Objetivo**: Imprimir o número `i` repetidamente em cada linha.
- **Explicação**:
  - `range(i)`: Cria uma sequência de `i` elementos.
  - `print(i, end=' ')`: Imprime o número `i` para cada elemento na sequência, seguido de um espaço, sem quebrar a linha.

### Finalizando a Linha:
```python
print()
```
- **Objetivo**: Pular para a próxima linha após a impressão de todos os números de uma linha da pirâmide.
- **Explicação**:
  - `print()`: Sem argumentos, `print` adiciona uma nova linha, movendo o cursor para o início da próxima linha.


## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Contato

Para dúvidas ou sugestões, entre em contato através do e-mail fingerdevfinger@gmail.com.
```

