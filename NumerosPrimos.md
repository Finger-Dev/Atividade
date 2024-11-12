# Verificação de Números Primos

Este projeto Python solicita ao usuário que insira um número inteiro *N* e, em seguida, exibe todos os números primos entre 1 e *N*. A verificação utiliza uma abordagem otimizada que itera apenas até a raiz quadrada de cada número para determinar se ele é primo.
Um número primo é um número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo sem deixar resto.
## Como Funciona

1. **Entrada do Usuário**: O programa solicita ao usuário que insira um número inteiro. Se a entrada não for um número inteiro válido, o programa solicitará novamente.
2. **Verificação de Primos**: Para cada número de 2 até *N*, o programa verifica se o número é primo iterando apenas até a raiz quadrada desse número.
3. **Resultado**: Todos os números primos encontrados entre 1 e *N* são exibidos ao usuário, até mesmo *N*, caso este também seja primo.

## Requisitos

- Python 3.x

## Como Usar

1. **Clone ou faça o download do repositório**:
   ```sh
   git clone https://github.com/Finger-Dev/Atividade.git
   cd Atividade
   ```
2. **Execute o programa:**
    ```sh
    python NumerosPrimos.py
    ```
3. **Siga as instruções do terminal:**
    * Digite um número maior ou igual a 2.
    * O programa exibirá todos os números primos entre 1 e o número fornecido pelo usuário.

## Exemplo de uso:
```sh
Digite um número inteiro: 20
Números primos entre  1 e 20:  [2, 3, 5, 7, 11, 13, 17, 19]
```
## Explicação do Algoritmo

Raiz Quadrada: Usamos  ` int(numero ** 0.5) + 1 `  para iterar apenas até a raiz quadrada de cada número, o que torna a verificação de primalidade mais eficiente, eliminando a necessidade de verificar divisores maiores que ela.

Loop Principal: Itera sobre cada número de 2 até 𝑁.

Verificação de Primos: Para cada valor, verifica se é divisível por qualquer número de 2 até a raiz quadrada desse número. Se não for divisível, é considerado primo.

Matemática usada em (numero ** 0.5): usa a lei dos expoentes na qual *N* elevado à potência 1/2 (ou 0.5) equivale a calcular a raiz quadrada de *N*. Por exemplo, o número 16 elevado à potência 0.5 equivale à raiz quadrada de 16, que é igual a 4.

Tratamento de Erros: O programa lida com entradas inválidas usando um bloco try-except para garantir que o usuário insira um número inteiro válido.

## Licença
Este projeto está licenciado sob a Licença MIT.

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Contato
Para dúvidas ou sugestões, entre em contato através do e-mail fingerdevfinger@gmail.com
