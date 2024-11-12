# Calculadora Simples

Este é um programa simples em Python que solicita ao usuário dois números e um operador (adição, subtração, multiplicação ou divisão) e realiza a operação correspondente. O programa lida com divisões por zero e operadores inválidos, solicitando ao usuário que insira os valores corretos.

## Requisitos

- Python 3.x
- Atualizar para acessar funcionalidades da versão 3.10

## Como Usar

1. **Clone ou faça o download do repositório:**
   ```sh
   git clone https://github.com/Finger-Dev/Atividade.git
   cd Atividade
   ```

2. **Execute o programa:**
    
    `python calculadora.py`

3. **Siga as instruções:** 

    Siga as instruções para realizar as entradas correspondentes

5. **Exemplo de uso:**
   ```sh
    Digite o primeiro número: 10
    Digite o segundo número: 5
    Digite o operador (+, -, *, /): +
    O resultado de 10.0 + 5.0 é: 15.0


## Funcionalidades

- Operações Básicas: Adição, subtração, multiplicação e divisão, através da escolha de caso (`match case`).

- Tratamento de Erros: Valida a entrada do operador e evita divisão por zero, utilizando `try` e `except ValueError`, além do `match case _:`
  e o `continue`. Importante alertar que a introdução do "Structural Pattern Matching", também conhecido como "match-case", só ocorreu a partir do Python 3.10. Portanto, é importante atualizar o software para acessar esta funcionalidade.

- `Loop` Repetição: através dos comandos `while` e `break`, permite que o usuário insira novos valores até que uma operação válida seja realizada. 

## Contribuindo
Se você deseja contribuir com este projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença
Este projeto é licenciado sob a Licença MIT.

## Contato
Para dúvidas ou sugestões, entre em contato pelo e-mail fingerdevfinger@gmail.com.
